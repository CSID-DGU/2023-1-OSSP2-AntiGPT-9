FROM python:3.10

WORKDIR /usr/src

COPY requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements.txt

EXPOSE 8010

COPY ./ /usr/src

CMD ["python", "main.py"]
