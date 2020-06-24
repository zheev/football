FROM python:3.7

WORKDIR /var/www

COPY ./requirements.txt /var/www/requirements.txt

RUN pip install -r /var/www/requirements.txt

COPY . /var/www

#CMD ["python3.7", "/var/www/server.py"]
CMD ["python3.7", "/var/www/test.py"]