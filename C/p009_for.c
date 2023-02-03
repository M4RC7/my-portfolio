#include  <stdio.h>
int main() {
  int n, i;
  char s[100];

  scanf("%d", &n);
  for (i = 0; n > 0; i++) { 
    s[i] = n % 10 + '0';
    n /= 10;
  }
  s[i] = '\0';
  printf ("\nInteiro positivo invertido: %s\n", s);

  return 0;
}
