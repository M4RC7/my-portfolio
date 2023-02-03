#!/bin/bash

if [ $# -eq 2 ]
then
if [ $1 -eq $2 ]
then
	echo -n "$1 igual a $2"
	echo ""
elif [ $1 -gt $2 ]
then
	echo -n "$1 maior que $2"
	echo ""
elif [ $1 -lt $2 ]
then
	echo -n "$1 menor que $2"
	echo ""
fi
else
	echo "Favor informar dois parâmetros:"
	echo "./s2.sh <p1> <p2>"
fi
