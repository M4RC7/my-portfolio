#!/bin/bash

i=1;
for arq in $(<frutas.txt)
do
	echo "Arquivo $i = $arq"
	i=$((i + 1))
done
