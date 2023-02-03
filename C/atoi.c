#include  <stdio.h>

#define MAX 10

int main() {
  char s[MAX];
  int i, n;

  scanf("%s", s);
  n = 0;
  for (i = 0; s[i] >= '0' && s[i] <= '9'; i++)
    n = 10 * n + (s[i] - '0');
  printf("\nValor inteiro: %i\n", n);

  return 0;
}
