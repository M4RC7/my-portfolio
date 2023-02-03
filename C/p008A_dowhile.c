#include  <stdio.h>

int main() {
  int n, i;
  char s[100];

  scanf("%d", &n);
  i = 0;
  do { 
    s[i] = n % 10 + '0';
    i++;
    n /= 10;
  } while (n > 0);
  s[i] = '\0';
  printf ("\nInteiro positivo invertido: %s\n", s);

  return 0;
}
