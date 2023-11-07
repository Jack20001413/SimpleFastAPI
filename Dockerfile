FROM python:3.11

WORKDIR /code

ENV AZURE_APPCONFIG_CONNECTION_STRING="Endpoint=https://appconfig-test-rg.azconfig.io;Id=8emh;Secret=IT+giUCpEZDcCjUktSSpgrhhIYk0rVcO+BW2dQD6EM8="

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]