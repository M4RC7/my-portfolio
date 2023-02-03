#!/bin/bash

clear
valor=0
while [ $valor -lt 50 ]
do
	echo -n "Digite um valor entre 0 e 100: "
	read valor
done
echo "Finalmente!"
