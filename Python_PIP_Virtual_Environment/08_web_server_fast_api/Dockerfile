FROM python:3.12

WORKDIR /my_super_app
COPY requirements.txt /my_super_app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . /my_super_app/

CMD ["uvicorn", "08_web_server_fast_api.08_fast_api:app", "0.0.0.0", "--port", "8585", "--reload"]