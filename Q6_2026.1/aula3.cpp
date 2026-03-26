#include <iostream>


// recebe xs[b:e) válido
// devolve a soma dos elementos de xs[b:e)
int soma(int *xs, size_t b, size_t e) {
    if (b == e) return 0;
    if (b + 1 == e) return xs[b];
    size_t m = (b + e)/2;
    int s = soma(xs, b, m);
    int t = soma(xs, m, e);
    return s + t;
}

// recebe: p[b:e) válido && e-b >= 2
// modifica: rearranja p[b:e) tal que p[b:i) <= p[i] < p[i+1:e) algum i em [b:e)
// devolve: i

size_t partition(int *p, size_t b, size_t e) {
    int x = p[b];
    size_t i = b;
    for (size_t k = b + 1; k != e; ++k) {
        if (p[k] <= x) {
            ++i;
            std::swap(p[k], p[i]);
        }
    }
    std::swap(p[b], p[i]);
    return i;
}

int *partition(int *b, int *e) {
    int x = *b;
    int *i = b;
    for (int *k = std::next(b); k != e; ++k) {
        if (*k <= x) {
            ++i;
            std::swap(*k, *i);
        }
    }
    std::swap(*b, *i);
    return i;
}

void qsort(int *b, int *e) {
    if (b == e || std::next(b) == e) return;
    int *i = partition(b, e);
    qsort(b, i);
    qsort(std::next(i), e);
}

void qsort(int *p, size_t b, size_t e) {
    if (b == e || b + 1 == e) return;
    size_t i = partition(p, b, e);
    qsort(p, b, i);
    qsort(p, i+1, e);
}

void qsort_v2(int *p, size_t b, size_t e) {
    while(true){
        if (b == e || b + 1 == e) return;
        size_t i = partition(p, b, e);
        qsort_v2(p, b, i);
        b = i + 1;
    }
}

void qsort_v2(int *b, int *e) {
    while(true){
        if (b == e || std::next(b) == e) return;
        int *i = partition(b, e);
        qsort_v2(b, i);
        b = std::next(i);
    }
}

int main(){
    int s[] = {543, 23, -23 , 42, 54, 45, 743, 45, 9, -32};
    std::cout << soma(s, 0, 10) << '\n';
    qsort_v2(std::begin(s), std::end(s));
    for (int x: s) std::cout << x << " ";
    return 0;
}