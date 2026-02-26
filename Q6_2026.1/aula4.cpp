#include <iostream>
#include <iterator>

// [b:m), [m:e) válidos
// *[b:m), *[m:e) ordenados
// rearranja [b:e) tal que após a chamada *[b:e) está ordenado
//
void merge (int *b, int *m, int *e, int *aux){
    int *i = b, *k = m, *d = aux;
    while (i != m && k != e) {
        if (*i <= *k) *d++ = *i++;
        else *d++ = *k++;
    }
    while (i != m) *d++ = *i++;
    while (k != e) *d++ = *k++;
    for (i = b; i != e; ++i) *i = *aux++;
    return;
}

void msort (int *b, int *e, int *aux) {
    size_t t = std::distance(b, e);
    if (t <= 1) return;
    int *m = b + t/2;
    msort (b, m, aux);
    msort(m, e, aux);
    merge (b, m, e, aux);
    return;
}

void msort (int *b, int *e) {
    size_t t = std::distance(b, e);
    if (t <= 1) return;
    int *aux = new int[t];
    msort (b, e, aux);
    delete [] aux;
    return;
}

void i_merge (int *x, size_t b, size_t m, size_t e, int *aux){
    size_t i = b, k = m, d = 0;
    while (i != m && k != e) {
        if (x[i] <= x[k]) aux[d++] = x[i++];
        else aux[d++] = x[k++];
    }
    while (i != m) aux[d++] = x[i++];
    while (k != e) aux[d++] = x[k++];
    for (i = b, d = 0; i != e; ++i) x[i] = aux[d++];
}

void i_msort (int *x, size_t b, size_t e, int *aux) {
    size_t t = e - b;
    if (t <= 1) return;
    size_t m = b + t/2;
    i_msort (x, b, m, aux);
    i_msort(x, m, e, aux);
    i_merge (x, b, m, e, aux);
}

void i_msort (int *x, size_t b, size_t e) {
    //std::cerr << " "; escreve mesmo quando der erro, então é usado para depurar
    size_t t = e - b;
    if (t <= 1) return;
    int *aux = new int[t];
    i_msort (x, b, e, aux);
    delete [] aux;
}

// x[b:b+s), x[b+s:b+2s), ..., x[b+ks:e) ordenado
// rearranjar de tal forma que se tenha blocos ordenados de tamanho 2s
// fazer a versão iterada do msort
void ite_merge (int *x, size_t b, size_t e, size_t s) {
    
}

/*
void msort (int *b, int *e) {
    size_t t = std::distance(b, e);
    if (t <= 1) return;
    int *m = b + t/2;
    msort (b, m);
    msort (m, e);
    merge (b, m, e);
}
*/

int main () {
    int x1[] = {1,4,2,0,9,5,6,3,8,10,7}, x2[] = {1,4,2,0,9,5,6,3,8,10,7};
    msort (std::begin(x1), std::end(x1));
    for (int x: x1) std::cout << x << ' ';
    std::cout << '\n';
    i_msort (x2, 0, 11);
    for (int x: x2) std::cout << x << ' ';
}