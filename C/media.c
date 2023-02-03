#include <stdio.h>
#include <stdlib.h>

int main()
{
  int tam;
  scanf("%d", &tam);

  int num[tam];
  int i;
  int soma=0;
  float media;

  for(i=0;i<tam;i++){
      scanf("%d", &num[i]);
  }

  for(i=0;i<tam;i++){
      soma+=num[i];
  }

  media = ((float)soma)/tam;
  printf("Posição... 6? %d\n", num[6]);
  printf("Done. %f\n", media);

  return 0;
}
