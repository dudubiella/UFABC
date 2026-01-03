#include<stdio.h>

int main (void){
    int n, soma = 0, i, j;
    printf ("Digite inteiros a serem somados (0 para sair):\n");
    scanf ("%d", &n);
    while (n != 0) { /*verifica antes*/
        soma += n;
        scanf("%d", &n);
    }
    printf ("Soma: %d\n", soma);
    
    printf ("Digite inteiros a serem somados (0 para sair):\n");
    soma = 0;
    do { /*verifica depois*/
        scanf("%d", &n);
        soma += n;
    } while (n != 0);
    printf ("Soma: %d\n", soma);
    
    for (i = 0; i <= 10; i++){
        printf ("%d\n", i);
    }
    
    for (j = 0, soma = 0; j <= 10; j++){
        soma += j;
        printf("%d\n", soma);
    }
    return 0;
}