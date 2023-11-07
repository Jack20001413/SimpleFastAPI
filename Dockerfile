FROM python:3.11

WORKDIR /code

ENV AZURE_APPCONFIG_CONNECTION_STRING=""

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app"]