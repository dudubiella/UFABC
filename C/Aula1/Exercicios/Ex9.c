#include <stdio.h>

int main (void) {
    
    int n, copia, contrario = 0;
    
    printf ("Escreva o numero possivel palindromo:\n");
    scanf ("%d", &n);

    copia = n;
    while (n >= 1) {
        contrario = contrario * 10 + n % 10;
        n /= 10;
    }
    
    if (copia == contrario) {
        printf ("%d e palindromo", copia);
    }
    else {
        printf ("%d nao e palindromo", copia);
    }

    return 0;
}