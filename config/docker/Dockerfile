FROM django

WORKDIR /drf-pyotp

ADD ./requirements.txt /drf-pyotp/requirements.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements.txt

ADD . /drf-pyotp

EXPOSE 80

COPY ./config/docker/docker-entrypoint.sh /
ENTRYPOINT ["./config/docker/docker-entrypoint.sh"]