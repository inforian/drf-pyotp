FROM django

WORKDIR /drf-pyotp

ADD ./requirements.txt /drf-pyotp/requirements.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements.txt
RUN pip install django-debug-toolbar

ADD . /drf-pyotp
