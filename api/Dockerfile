FROM python:3.10.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
ADD requirements.txt /api/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
ADD . /api/
# Django service
EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]