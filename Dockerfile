FROM python:3.12-slim

COPY requirements.txt /src/
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]