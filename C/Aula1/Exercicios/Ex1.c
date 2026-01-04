#include <stdio.h>

int main (void) {

    /* Exercício 01 */

    int n, fat;
    int m, div;

    printf ("\nEscolha um numero 'n' para o calculo do seu fatorial:\n");
    scanf ("%d", &n);

    fat = 1;
    while (n > 1){
        fat *= n--;
    }
    
    printf ("n! = %d\n", fat);

    return 0;
}