#include<stdio.h>
#include<stdbool.h>

int main (void) {
    bool a = true, b = false;
    printf ("a && b (a e b) = %d\n", a && b);
    printf ("a || b (a ou b) = %d\n", a || b);
    printf ("!a (nao a) = %d\n", !a);
    printf ("b tq a = %d\n", !a || (a && b));
    return 0;
}