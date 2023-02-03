#!/bin/bash
# marcos aqui é usado como exemplo de nome de usuário.
echo "Quantidade de arquivos em /home/$(whoami): "ls -R ~ | wc -l
