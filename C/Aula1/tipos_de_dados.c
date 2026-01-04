#include <stdio.h>

int main(void) {
    int a = 10;
    unsigned int b = 020;
    float d = 3.14f;
    char e = 'A';
    
    printf ("%d %u %f %d\n", a, b, d, e);
    printf ("char %lu\n",sizeof(char));
    printf ("int %lu\n",sizeof(short));
    printf ("int %lu\n",sizeof(int));
    printf ("long int %lu\n",sizeof(long int));
    printf ("long long int %lu\n",sizeof(long long int));
    printf ("float %lu\n",sizeof(float));
    printf ("double %lu\n",sizeof(double));
    printf ("long double %lu\n",sizeof(long double));
    
    int c = (int) d;
    printf ("%d\n", c);

    a = 50000;
    short f = (short) a;
    printf ("%d\n", f);

    double g = 2/5;
    printf ("%f\n", g);

    return 0;
}