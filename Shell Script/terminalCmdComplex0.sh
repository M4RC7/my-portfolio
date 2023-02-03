#!/bin/bash
# escrever 59 23 * * 1 (username) (diretório)/ex10.sh
# em crontab para programá-lo
echo "Compactar a pasta 'trabalhos'."
zip trabalhos.zip trabalhos
echo "Remover a pasta 'trabalhos'."
rm -i trabalhos
