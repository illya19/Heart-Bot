FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y git
WORKDIR /app
RUN git clone https://github.com/illya19/Heart-Bot.git && \
    cd Heart-Bot && \
    pip install aiogram
CMD ["python", "-m", "main"]
