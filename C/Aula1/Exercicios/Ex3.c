#include <stdio.h>

int main (void) {
    
    /*Exercício 03*/

    int n, i, x, maior, menor, impar = 0, par = 0;

    printf ("Escolha quantos numeros serao considerados:\n");
    scanf ("%d", &n);
    printf ("Agora escreva cada um dos %d numeros\n\n");

    for (i = 1; i <= n; i++) {
        printf ("Escolha o %d numero: ", i);
        scanf ("%d", &x);
        if (i == 1) {
            maior = menor = x;
        }
        else {
            if (x > maior) {
                maior = x;
            }
            if (x < menor) {
                menor = x;
            }
        }
        if (x % 2 == 0) {
            par++;
        }
        else {
            impar++;
        }
    }

    printf("\nImpares: %d\nPares: %d\nMaior: %d\nMenor: %d\n", impar, par, maior, menor);

    return 0;
}