#!/bin/bash

echo -n "Digite o diretório a ser verificado: "
read verifDir
rm -i $verifDir/*.tmp
echo "Arquivos temporários apagados"
