#include <stdio.h>

int main (void) {
    
    int opcao = 0;
    float a, b, c;

    do {
        printf ("Escolha uma das opcoes:\n\n1: soma dois numeros (a + b);\n2: soma tres numeros (a + b + c);\n3: multiplicacao de dois numeros (a * b);\n0: sair.\n");
        scanf ("%d", &opcao);
        
        switch (opcao) {
            case (1): {
                printf ("\nEscolha os numeros 'a' e 'b':\n");
                scanf ("%f %f", &a, &b);
                printf ("%.3f + %.3f = %.4f\n\n", a, b, (float) a + b);
                break;
            }
            case (2): {
                printf ("\nEscolha os numeros 'a', 'b' e 'c':\n");
                scanf ("%f %f %f", &a, &b, &c);
                printf ("%.3f + %.3f + %.3f = %.4f\n\n", a, b, c, (float) a + b + c);
                break;
            }
            case (3): {
                printf ("\nEscolha os numeros 'a' e 'b':\n");
                scanf ("%f %f", &a, &b);
                printf ("%.3f * %.3f = %.5f\n\n", a, b, (float) a * b);
                break;
            }
            
        }
    } while (opcao != 0);

    return 0;
}