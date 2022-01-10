#FROM centos:centos7
FROM docker-registry.prosper2.net:5000/official/centos:centos7
RUN yum install -q -y epel-release && \
    yum install -q -y --enablerepo=epel python3 python3-pip python3-devel mariadb-devel gcc && \
    rm -rf /var/cache/yum/* && \
    yum clean all && \
    pip3 install --upgrade pip && \
    pip3 install fastapi uvicorn mysqlclient sqlalchemy aiofiles Jinja2 sqlmodel bottle uwsgi

RUN mkdir /tmp/run
ENV LC_ALL=en_US.UTF-8
ENTRYPOINT ["uwsgi","--ini","emperor.ini"]

# キャッシュ対策のため可変コンテンツは最後のほうにしておく
WORKDIR /uwsgi
COPY ./uwsgi ./
