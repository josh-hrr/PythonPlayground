FROM python:3.12

WORKDIR /my_super_app
COPY requirements.txt /my_super_app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . /my_super_app/

CMD bash -c "while true; do sleep 1; done"