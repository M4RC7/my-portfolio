#!/bin/bash

i=1;
for arq in $(</etc/passwd)
do
  echo "Logins: "
  cut -d: -f1 /etc/passwd
  i=$((i + 1))
done
