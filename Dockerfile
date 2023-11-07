FROM python:3.11

WORKDIR /code

ENV AZURE_APPCONFIG_CONNECTION_STRING="Endpoint=https://demo-van-sea-ac.azconfig.io;Id=63Wy;Secret=PPpc0NRUm8P63p6BZcTmqzR66jc/ZpDvlo0iuzY+V0c="

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]