FROM tiangolo/uwsgi-nginx-flask:python3.8

# App
COPY ./app /app

# Dataset
RUN mkdir -p /app/data/top
COPY ./data/top/dataset_final.csv /app/data/top

# Static files
COPY ./static /app/static
ENV STATIC_INDEX 1
