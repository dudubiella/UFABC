#include <stdio.h>

int main (void) {

    int n, i, xi, soma = 0, soma2 = 0;

    printf ("Escreva quantos numeros serao usados para calcular a variancia:\n");
    scanf ("%d", &n);

    if (n < 2) {
        printf("n deve ser pelo menos 2 para calcular variancia.\n");
        return 1;
    }

    printf ("Agora escreva cada numero:\n\n");
    
    for (i = 0; i < n; i++){
        printf ("Digite o inteiro: ");
        scanf ("%d", &xi);
        soma += xi;
        soma2 += xi * xi;
    }
    printf ("\nA media deles e: %.3f\nA variancia entre eles e: %.3f\n", (float) soma / n , (float) soma2 / (n - 1) - (float) soma * soma / (n * (n - 1)));

    return 0;
}