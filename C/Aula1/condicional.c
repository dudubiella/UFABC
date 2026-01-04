#include <stdio.h>

int main (void){
    int n, a, b;
    char op;
    printf ("Digite um inteiro:\n");
    scanf ("%d", &n);

    if (n % 2 == 0){
        printf ("%d e par.\n", n);
    }
    else{
        printf ("%d e impar.\n", n);
    }

    if (n < 0){
        printf ("%d e negativo.\n", n);
    }
    else if (n > 0){
        printf ("%d e positivo.\n", n);
    }
    else{
        printf ("%d e zero\n", n);
    }
    
    printf ("\nDigite uma operacao no formato a op b:");
    scanf ("%d %c %d", &a, &op, &b);
    
    switch (op){
        case '+':
            printf ("%d + %d = %d", a, b, a + b);
            break;
        case '-':
            printf ("%d - %d = %d", a, b, a - b);
            break;
        case '*':
            printf ("%d * %d = %d", a, b, a * b);
            break;
        case '/':
            printf ("%d / %d = %d", a, b, a / b);
            break;
        default:
            printf("Erro: operador invalido!\n");
            break;
    }
    
    return 0;
}
