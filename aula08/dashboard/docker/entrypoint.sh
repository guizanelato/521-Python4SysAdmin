#!/bin/bash 

echo "iniciando o serviço do apache"
service apache2 start

echo "amarrando o container ao acess log ..."
tail -f /var/log/apache2/access.log
