FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY stopwords.txt /app/stopwords.txt

COPY run.py /app/run.py

CMD ["fastapi", "run", "/app/run.py", "--port", "8080"]
