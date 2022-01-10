#!/bin/bash

# スクリプトが配置されているディレクトリの一階層上に移動する。
cd $(dirname $0)/..

export K8S_NAMESPACE=myapp
export REPO_NAME=`pwd | sed 's/..*\///'`


################################################
# コンフィグマップを以下のように作成する
#   入力ファイル： ./deploy/config/*
#   テンプレート： ./deploy/tmpl/configmap.tmpl
#   出力ファイル： ./deploy/*.yaml
################################################
echo '##### K8S YAML GENERATOR #####'
files=`find ./deploy/config -maxdepth 1 -type f -not -name '.*' -not -name '_*' |sort`

for file_path in $files;
do
  file_name=${file_path##*/}
  export TMP_CONFIG_KEY_NAME=${file_name/./-}
  export TMP_CONFIG_FILE_NAME=$file_name
  export TMP_CONFIG_BODY=`envsubst '' < ./deploy/config/$file_name | sed 's/\(.*\)/\ \ \ \ \1/g'`
  envsubst '${K8S_NAMESPACE} ${REPO_NAME} ${TMP_CONFIG_KEY_NAME} ${TMP_CONFIG_FILE_NAME} ${TMP_CONFIG_BODY}' < ./deploy/tmpl/configmap.tmpl > ./deploy/02config_$file_name.yaml
  echo "  create 02config_$file_name.yaml"
done

########################
# K8Sデプロイ用のファイルを以下のように作成する
#   テンプレート： ./deploy/tmpl/*
#   出力ファイル： ./deploy/*.yaml
########################
files=`find ./deploy/tmpl -maxdepth 1 -type f -not -name configmap.tmpl -not -name '.*'|sort`

for file_path in $files;
do
  file_name=${file_path##*/}
  envsubst  < ./deploy/tmpl/$file_name > ./deploy/$file_name.yaml

  echo "  create $file_name.yaml"

done

