#include<stdio.h>

float setValue(){
  float x;
  printf("Insira um valor real: ");
  scanf("%f", &x);
  return (x);
}

int main(){
  float v = setValue();
  double d = 240.0;

  printf("\n\tFloat: %f", v);
  printf("\n\tDouble: %f", d);
  printf("\n\tFloat em notação científica: %e", v);
  printf("\n\tDouble em notação científica: %E\n", d);

  return 0;
}
