FROM python:3.10-slim-buster
COPY . .

# RUN apt update -y && apt install awscli -y

RUN pip install -r Requirements.txt
CMD ["python3", "app.py"]