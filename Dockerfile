FROM tangchen2018/python:3.6-alpine
ENV PYTHONUNBUFFERED 1

COPY . /project/server

WORKDIR /project/server

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk add --no-cache tzdata build-base libffi-dev openssl-dev python-dev py-pip && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

RUN pip install -i https://pypi.douban.com/simple --upgrade pip \
    && pip install -r requirements.txt -i https://pypi.douban.com/simple \
    && mkdir -p /project/server/logs

CMD python /project/server/taskmain.py
#CMD ["python", "/project/sso/manage.py crontab remove"]
#CMD ["python", "/project/sso/manage.py crontab add"]
