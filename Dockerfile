FROM django
ADD . /drf-pyotp

WORKDIR /drf-pyotp

#RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements.txt
RUN pip install django-debug-toolbar
