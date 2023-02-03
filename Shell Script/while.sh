#!/bin/bash

echo "Informe um valor positivo: "
read valor;
if [ $valor -lt 1 ]
then
  echo "Valor invalido."
else
  resultado=1
while [ $valor -ne 1 ]
do
  $resultado = $(($resultado * $valor))
  $valor = $valor - 1
done
echo -n "Resposta encontrada: "
echo "$resultado"
fi
