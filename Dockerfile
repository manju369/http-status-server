# temp stage
FROM python:3.10-slim as builder


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY app /app
WORKDIR /app
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /opt/wheels -r pip-requirements.txt
RUN pip3 install --no-cache /opt/wheels/*
RUN python3 -m unittest test_server.py 
RUN echo "test successfull"
RUN rm -rf /app/test_*




# final stage
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /opt/wheels /wheels
COPY --from=builder /app /app

RUN pip3 install --no-cache /wheels/*
RUN useradd flask 

RUN chown -R flask /app/
USER flask

EXPOSE 5000
CMD ["python3" , "/app/server.py"]

