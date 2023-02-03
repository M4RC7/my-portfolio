/* Converte maiúscula para minúscula */

#include <stdio.h>

int main() {
  char c, min;

  scanf("%c", &c);
  if (c >= 'A' && c <= 'Z') {
    min = c + 'a' - 'A';
    printf("\nMinuscula: %c\n", min);
  }
  else
    printf ("\nNao e' maiuscula: %c\n", c);

  return 0;
}
