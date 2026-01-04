#include <stdio.h>

int main (void) {

    /* Exercício 02 */

    int m, div;
    
    printf ("\nEscreva um numero positivo para imprimir seus divisores:\n");
    scanf ("%d", &m);
    
    printf ("Os divisores de %d sao:\n", m);
    for (div = m; div > 0; div--) {
        if (m % div == 0) {
            printf ("%d\n", div);
        }
    }

    return 0;
}