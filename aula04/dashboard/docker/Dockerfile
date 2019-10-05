FROM ubuntu

WORKDIR /app

RUN apt update && apt install apache2 -y #executado na criação da imagem

COPY entrypoint.sh /app/entrypoint.sh

COPY html /var/www/html

ENTRYPOINT ["/bin/bash" , "/app/entrypoint.sh"]
