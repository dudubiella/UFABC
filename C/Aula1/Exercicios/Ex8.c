#include <stdio.h>

int main (void) {
    
    int n, soma;
    printf ("Escreva o numero a se somado os algarismos:\n");
    scanf ("%d", &n);

    if ((int) n / 10 == 0) {
        printf ("Erro: Numero com apenas um algarismo");
    }
    else {
        printf ("\nSomas:\n");

        while ((int) n / 10 != 0) {
            soma = 0;

            while ((int) n / 10 != 0) {
                soma += n % 10;
                n = (int) n / 10;
            }

            soma += n;
            printf ("%d\n", soma);
            n = soma;
        }
    }

    return 0;
}