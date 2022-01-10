#!/bin/bash

# スクリプトが配置されているディレクトリの一階層上に移動する。
cd $(dirname $0)/..

files=`find ./deploy/ -maxdepth 1 -type f -name *.yaml -not -name '.*' | sort`

for file_path in $files;
do
  kubectl apply -f $file_path
done

