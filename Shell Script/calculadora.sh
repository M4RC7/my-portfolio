#!/bin/sh
# calculadora 
# 2 de julho de 2003
# http://msanet.port5.com
# Marcelo Santos Araujo - msa@nanet.com.br
clear
echo -e "\t\tCalculadora Simples\n"
echo -e "\t\t(1) - Soma\n\t\t(2) - Subtracao\n\t\t(3) - Multiplicacao\n\t\t(4) - Divisao\n\t\tPressione (1/2/3/4):"
read opcao

if [ $opcao -eq 1 ]; then
   echo "Digite o valor 1: "
   read valor1
   echo "Digite o valor 2: "
   read valor2
   echo "Resultado:"
   echo "scale=2;($valor1 + $valor2)" | bc
elif [ $opcao -eq 2 ]; then
     echo "Digite o valor 1: "
     read valor1
     echo "Digite o valor 2: "
     read valor2
     echo "Resultado:"
     echo "scale=2;($valor1 - $valor2)" | bc
elif [ $opcao -eq 3 ]; then
     echo "Digite o valor 1: "
     read valor1
     echo "Digite o valor 2: "
     read valor2
     echo "Resultado:"
     echo "scale=2;(($valor1) * ($valor2))" | bc
elif [ $opcao -eq 4 ]; then
     echo "Digite o valor 1: "
     read valor1
     echo "Digite o valor 2: "
     read valor2
     echo "Resultado:"
     echo "scale=2;(($valor1)/($valor2))" | bc
else
echo -e "Opcao invalida!\n\n"
fi
