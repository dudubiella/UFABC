#include <stdio.h>
#include <stdbool.h>
#include <math.h>

unsigned unsigned_sqrt (unsigned n);
bool e_primo (unsigned n);
void imprime_primos (unsigned n);

unsigned unsigned_sqrt (unsigned n) {
    return (unsigned) sqrt ((double) n);
}

bool e_primo (unsigned n) {
    
    unsigned i;
    bool r = true;

    for (i = 2; i <= unsigned_sqrt (n); i++) {
        if (n % i == 0) r = false;
    }

    return r;
}

void imprime_primos (unsigned n) {

    unsigned i;

    for (i = 2; i <= n ; i++) {
        if (e_primo (i)) {
            printf ("%u\n", i);
        }
    }
}

int main (void) {
    
    unsigned n;

    printf ("Digite um numero inteiro positivo para imprimir os peimos ate ele: ");
    scanf ("%u", &n);

    imprime_primos (n);

    return 0;
}