FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

# App
COPY ./app /app

# Dataset
RUN mkdir -p /app/data/top
COPY ./data/top/dataset_final.csv /app/data/top

# Static files
COPY ./static /app/static
ENV STATIC_INDEX 1
