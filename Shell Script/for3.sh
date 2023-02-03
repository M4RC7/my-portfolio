#!/bin/bash

i=1;
for arq in $(ls)
do
	echo $(file $arq)
	i=$((i + 1))
done
