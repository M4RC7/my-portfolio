#include  <stdio.h>

int main() {
  int c;

  scanf("%i", &c);
  while (c >= 0 && c <= 100) {
    printf("\nOK!: %d\n", c);
    scanf("%i", &c);
  }
  if (c < 0 || c > 100)
    printf ("\nFora do intervalo: %i\n", c);

  return 0;
}
