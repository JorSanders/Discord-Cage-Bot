FROM python:3.12.0a3-alpine

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache build-base &&\
    pip install --no-cache-dir -r /tmp/requirements.txt &&\
    rm -rf /tmp/requirements.txt

COPY jorkol /usr/local/app/jorkol
ENV LOG_LEVEL "INFO"

WORKDIR /usr/local/app
ENTRYPOINT ["sh", "-c", "python -m jorkol.discord_cage_bot.src.discord_cage_bot --log \"$LOG_LEVEL\""]
