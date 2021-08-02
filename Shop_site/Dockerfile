From python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/My_site

COPY ./lib.txt /usr/src/lib.txt
RUN pip install -r /usr/src/lib.txt
#COPY . /usr/src/My_site

EXPOSE 8000

