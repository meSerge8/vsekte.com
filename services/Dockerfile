FROM python:3
EXPOSE 2345
WORKDIR /app
RUN apt update && apt install -y postgresql-client && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 2345
CMD ["python3", "main.py"]
