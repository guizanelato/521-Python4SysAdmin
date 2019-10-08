
# Comentários
FROM ubuntu 

#diretorio de trabalho
WORKDIR /app


RUN apt update && apt install -y vim python3-pip 

COPY . /app

RUN pip3 install -r /app/requirements.txt

CMD [ "python3" , "/app/app.py" ]

