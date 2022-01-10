#!/bin/bash

# スクリプトが配置されているディレクトリの一階層上に移動する。
cd $(dirname $0)/..

K8S_NAMESPACE=myapp
REPO_NAME=`pwd | sed 's/..*\///'`

################################################
# dockerイメージをビルドしてpushする
################################################
echo '##### DOCKER IMAGE BUILDER #####'
docker build . -f ./Dockerfile -t docker-registry.prosper2.net:5000/${K8S_NAMESPACE}/$REPO_NAME:latest
docker push docker-registry.prosper2.net:5000/${K8S_NAMESPACE}/$REPO_NAME:latest

echo $(date +%s)
