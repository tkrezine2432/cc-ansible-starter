FROM public.ecr.aws/docker/library/python:3.12-slim
RUN pip install --no-cache-dir pymysql==1.1.1 cryptography==50.0.2
COPY store.py /app/store.py
EXPOSE 8080
CMD ["python", "/app/store.py"]
