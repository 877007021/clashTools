FROM python:3.10.11

WORKDIR /app
COPY . /app

RUN pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

CMD ["python", "main.py"]