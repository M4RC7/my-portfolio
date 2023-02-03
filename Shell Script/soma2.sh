#!/bin/bash

if [ $# -eq 2 ]
then
	echo -n "A soma é "
	echo $(($1 + $2))
else
	echo "Favor digitar dois parâmetros."
	echo "Formato: ./soma2.sh <num1> <num2>"
fi
