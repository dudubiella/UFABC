#include <stdio.h>

int main (void) {

    /* Exercício 00 */

    int a, b, temp;

    printf ("Escolha dois inteiros para o calculo do MDC deles:\n");
    scanf ("%d %d", &a, &b);
    
    if (b > a) {
        printf ("%d %d", a, b);
        temp = a;
        a = b;
        b = temp;
    }
    
    while (a % b != 0){
        temp = a % b;
        a = b;
        b = temp;
    }
    
    printf ("MDC = %d\n", b);

    return 0;
}