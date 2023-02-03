#include<stdio.h>

int main(){
  char c;
  char string[30];
  //char string[]= "Hello"; //only works this way

  printf("\n\tDigite um caractere: ");
  scanf("%c", &c);
  printf("\n\tDigite seu nome: ");
  scanf("%s", string);
  printf("\n\tCaractere: %c\n",c);
  printf("\n\tCaractere como número: %d\n",c);
  printf("\n\tString: %s\n",string);

  return 0;
}
