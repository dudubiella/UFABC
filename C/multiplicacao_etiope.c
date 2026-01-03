#include <stdio.h>

int mult_etiope (int x, int y) {
    int z = 0;
do {
    if (x % 2 == 1)
        z = z + y;
    x = x / 2;
    y = 2 * y;
    } while (x >= 1);
    return z;
}

int main (void) {
    int x, y, r;
    printf ("primeiro numero a ser multiplicado:\n");
    scanf ("%d", &x);
    printf ("segundo numero:\n");
    scanf ("%d", &y);
    r = mult_etiope (x, y);
    printf ("resultado:\n%d\n", r);
    return 0;
}