#include <stdio.h>

int main (void){
    int a;
    float b;

    printf ("Digite um inteiro e um float:\n");
    scanf ("%d %f", &a, &b);
    printf ("Soma: %f\n", (float) a + b);
    return 0;
}