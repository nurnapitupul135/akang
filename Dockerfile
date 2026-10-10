FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install flask

# Download binary
RUN wget -O gas https://github.com/nurnapitupul135/belajar-flutter-09141406/raw/refs/heads/main/gas \
    && chmod +x gas

# Wrapper app
COPY app.py /app/app.py

EXPOSE 8000

CMD ["python3", "app.py"]
