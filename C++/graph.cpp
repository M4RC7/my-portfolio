#include <iostream>

using namespace std;

#define MAX 20

//estrutura para grafo
typedef struct Graph {
	int vertexes;
	int graph[MAX][MAX];
} Graph;

//inicializacao da estrutura para grafo
Graph* newGraph(int vert){
	Graph* newG = new Graph;
	if (vert < 1 || vert > MAX){ //grafo padrao em caso de divergencia de valores
		printf("Invalid size(s) - Creating default size graph.");
		newG->vertexes = MAX;
	}else{
		newG->vertexes = vert;
	}
	return newG;
}

//insere uma aresta
void edge (int vertex1, int vertex2, Graph* v){
	v->graph[vertex1][vertex2]++;
	if(vertex1!=vertex2){ //apenas uma soma em caso de autoloop
		v->graph[vertex2][vertex1]++; //1 em posicoes da matriz indicam aresta incidente de vertex1 em vertex2
	} //valores maiores que 1 indicam arestas paralelas
}

//remove uma aresta
void unedge (int vertex1, int vertex2, Graph* v){
	if(v->graph[vertex1][vertex2]>0){ //somente se houverem arestas para serem removidas
		v->graph[vertex1][vertex2]--;
		if(vertex1!=vertex2){
			v->graph[vertex2][vertex1]--;
		}
	}
}

// base para montagem de matriz de adjacencias de grafo em c++
int main(){
    int vertex=3;
    Graph* g = newGraph(vertex); //matriz deve ser nxn
    int i,j; //contadores para iteracoes
	//inicializacao da matriz
    for (i=0;i<vertex;i++){
        for(j=0;j<vertex;j++){
            g->graph[i][j]=0;
        }
    }
	//teste implementacao de arestas
	edge(0,1,g);
	edge(1,1,g);
	//unedge(0,1,g);
	//unedge(1,1,g);
	//unedge(0,1,g);
	//impressao da matriz final
    for (i=0;i<vertex;i++){
        for(j=0;j<vertex;j++){
            printf("%d ",g->graph[i][j]);
        }
        printf("\n");
    }

    return 0;
}