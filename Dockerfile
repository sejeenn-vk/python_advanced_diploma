FROM python:3.12-slim
WORKDIR /home
COPY requirements.txt src/
RUN pip install --upgrade pip
RUN pip install -r /home/src/requirements.txt

COPY src src/
COPY static static/

EXPOSE 8000

CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
