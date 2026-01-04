#include <stdio.h>

int main (void) {

    int xi, soma = 0, soma2 = 0;

    printf ("Escreva numeros inteiros positivos para o calculo da  diferenca entre a soma dos quadrados e o quadrado da soma entre eles, para concluir digite '-1':\n\n");
    do {
        printf ("Digite o inteiro: ");
        scanf ("%d", &xi);
        soma += xi;
        soma2 += xi * xi;
    } while (xi >= 0);
    printf ("Resultado: %d\n", soma2 - soma * soma);

    return 0;
}