FROM python:3.8-slim-buster
RUN apt-get update && apt-get install git -y
WORKDIR /app
RUN git clone https://github.com/illya19/Heart-Bot.git && cd Heart-Bot && pip install aiogram
CMD ["python3", "-m", "main"]
