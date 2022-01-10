# fastapi


## deploy ( kubernetes )


```
# set namespace
kubectl config set-context $(kubectl config current-context) --namespace=myapp

# unset namespace
kubectl config set-context $(kubectl config current-context) --namespace=default
```

Set OAuth2-Proxy Environment variables.( [oauth2-proxy.github.io/oauth2-proxy](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/overview/#environment-variables) )

environment variables are referenced from:  
[main-repo:environment](https://github.com/bashaway/k8s-myapp/blob/main/main-repo/deploy/tmpl/environment#L7-L9)  

```
# set environment
export K8S_OAUTH2_PROXY_CLIENT_ID=...
export K8S_OAUTH2_PROXY_CLIENT_SECRET=...
export K8S_OAUTH2_PROXY_COOKIE_SECRET=`python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'`
```

build

```
# docker build and push
./main-repo/_build/docker_build.sh
./fastapi-repo/_build/docker_build.sh
./uwsgi-repo/_build/docker_build.sh

# make yaml files
./main-repo/_build/k8s_makeyaml.sh
./fastapi-repo/_build/k8s_makeyaml.sh
./uwsgi-repo/_build/k8s_makeyaml.sh

# docker build and push
./main-repo/_build/k8s_deploy.sh
./fastapi-repo/_build/k8s_deploy.sh
./uwsgi-repo/_build/k8s_deploy.sh

```

delete resource

```
# docker build and push
./main-repo/_build/k8s_delete.sh
./fastapi-repo/_build/k8s_delete.sh
./uwsgi-repo/_build/k8s_delete.sh

```


## debug ( docker-compose )

Set OAuth2-Proxy Environment variables.( [oauth2-proxy.github.io/oauth2-proxy](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/overview/#environment-variables) )

environment variables are referenced from:  
[docker-compose.yaml](https://github.com/bashaway/k8s-myapp/blob/main/docker-compose.yaml#L72-L74)

```
# set environment
export OAUTH2_PROXY_CLIENT_ID=...
export OAUTH2_PROXY_CLIENT_SECRET=...
export OAUTH2_PROXY_COOKIE_SECRET=`python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'`
```

build

```
docker-compose -f docker-compose.yaml up --build 

```


# Docker Images

## copy official image to private registry

```
IMAGE=alpine:latest
docker pull ${IMAGE}
docker tag ${IMAGE} docker-registry.prosper2.net:5000/official/${IMAGE}
docker push docker-registry.prosper2.net:5000/official/${IMAGE}

```


## delete docker containers and images

```
sudo docker rm $(sudo docker ps -a -q) -f
sudo docker rmi $(sudo docker images -q) -f
sudo docker volume rm $(sudo docker volume ls -qf dangling=true)

```

