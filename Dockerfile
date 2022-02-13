FROM python:3.10-alpine

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache gcc  &&\
    pip install --no-cache-dir -r /tmp/requirements.txt &&\
    rm -rf /tmp/requirements.txt

COPY jorkol /usr/local/app/jorkol
WORKDIR /usr/local/app
ENTRYPOINT ["python", "-m", "jorkol.discord_cage_bot.src.discord_cage_bot"]
