#include <stdio.h>

int main (void) {

    int n, i, fib = 0, f0 = 0, f1 = 1;

    printf ("Escolha um numero n para o calculo do n-esimo numero da sequencia de Fibonacci:\n");
    scanf ("%d", &n);

    if (n == 1) {
        printf ("F%d = 1\n", n);
    }
        else {
        for (i = 2; i <= n; i++) {
            fib = f0 + f1;
            f0 = f1;
            f1 = fib;
        }
        printf ("F%d = %d\n", n, fib);
    }

    return 0;
}