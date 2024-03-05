#include <stdio.h>
#include <stdlib.h>

int main() {
// definir dados
   int i, j, m, n;
   FILE *obj = fopen ("tabela.txt", "w");
// verificar se arquivo foi aberto
   if (obj != NULL) {
   // ler valores para tamanho
      printf("Dimensoes:");
      scanf("%d", &m);
      scanf("%d", &n);
      fprintf (obj, "%d ", m);
      fprintf (obj, "%d\n", n);
   // gerar valores para matriz
      for (i = 0; i < m; i++) {
         for (j = 0; j < n; j++) {
            fprintf (obj, "%d ", rand() % 1000);
         }
         fprintf(obj, "\n");
      }
   // fechar arquivo (indispensavel)
      fclose(obj);
      printf("Sua tabela foi criada.\n");
   }
   return 0;
}
