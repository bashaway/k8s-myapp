#FROM centos:centos7
FROM docker-registry.prosper2.net:5000/official/centos:centos7
RUN yum install -q -y epel-release && \
    yum install -q -y --enablerepo=epel nginx php php-fpm python3 python3-pip python3-devel gcc ruby fcgi spawn-fcgi fcgiwrap perl perl-CGI && \
    rm -rf /var/cache/yum/* && \
    yum clean all 

RUN mkdir -p /opt/tmp/html && mkdir -p /var/www/html
ENV LC_ALL=en_US.UTF-8
COPY ./config/php-fpm.conf /etc/php-fpm.conf
COPY ./config/php.ini /etc/php.ini
COPY ./config/www.conf /etc/php-fpm.d/www.conf

# キャッシュ対策のため可変コンテンツは最後のほうにしておく
WORKDIR /opt/tmp/html
COPY ./html ./
