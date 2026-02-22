#include <stdio.h>

int main (void) {
    
    int i, n = 10, numeros [10] = {3, 2, 1}, num2 [3] = {[2] = 3, [0] = 2};

    numeros [7] = 4;

    for (i = 0 ; i < n; i ++) {
        printf ("numero %d: %d\n", i, numeros [i]);
    }

    printf ("\nDigite o tamanho da lista: ");
    scanf ("%d", &n);

    int tam_variavel [n];       /*Variable Length Arrays (VLA) (Lista de Tamanha Variavel)*/

    for (i = 0 ; i < n; i ++) {
        printf ("Digite o %d numero inteiro:\n", i);
        scanf ("%d", &tam_variavel[i]);
    }

    for (i = 0 ; i < n; i ++) {
        printf ("numero %d: %d\n", i, tam_variavel [i]);
    }

    return 0;
}