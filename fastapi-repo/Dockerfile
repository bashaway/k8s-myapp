#FROM centos:centos7
FROM docker-registry.prosper2.net:5000/official/centos:centos7
RUN yum install -q -y epel-release && \
    yum install -q -y --enablerepo=epel python3 python3-pip python3-devel mariadb-devel gcc && \
    rm -rf /var/cache/yum/* && \
    yum clean all && \
    pip3 install --upgrade pip && \
    pip3 install fastapi uvicorn mysqlclient sqlalchemy aiofiles Jinja2 sqlmodel bottle uwsgi

ENV LC_ALL=en_US.UTF-8
ENV FASTAPI_PATH_PREFIX=/api/fastapiapp
# mysqlのDockerコンテナを準備するときはinit.sqlの流し込みが完了するタイミングまでsleepする
ENTRYPOINT ["sh", "-c", "sleep 3 && ./_generator/tmpl.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
#ENTRYPOINT ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000"]
#ENTRYPOINT ["/sbin/init"]

# キャッシュ対策のため可変コンテンツは最後のほうにしておく
WORKDIR /fastapi
COPY ./fastapi ./
