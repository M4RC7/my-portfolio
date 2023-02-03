#!/bin/bash

i=1;
for arq in $(ls)
do
	echo "Arquivo $i = $arq"
	i=$((i + 1))
done
