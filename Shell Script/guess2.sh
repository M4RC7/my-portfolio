#!/bin/bash

clear
valor=$RANDOM
chute=-1

while [ $valor -ne $chute ]
do
	echo -n "Acerte um valor entre 0 e 32767: "
	read chute
	if [ $chute -gt $valor ]
	then
		echo "Menor"
	else
		if [ $chute -lt $valor ]
		then
			echo "Maior"
		fi
	fi
	
done
echo "Finalmente!"
