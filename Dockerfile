FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD ./req.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/req.txt
ADD ./ /app/
