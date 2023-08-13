FROM ubuntu:latest
RUN apt-get update && apt install git wget python3-pip -y
RUN git clone https://github.com/illya19/Heart-Bot && cd Heart-Bot && pip install aiogram
CMD ["python3", "-m", "main"]
