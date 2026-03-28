#include <iostream>
#include <iterator>
#include <utility>

// recebe xs[b:e) válido
// devolve  a soma dos elementos de xs[b:e)
int soma(int *xs, size_t b, size_t e) {
    if (b == e) return 0;
    if (b + 1 == e) return xs[b];
    size_t m = (b + e)/2; // aqui b < m < e
    int s = soma(xs, b, m);
    // s é a soma dos elementos de xs[b:m)
    int t = soma(xs, m, e); 
    // t é a soma dos elementos de xs[m:e)
    return s + t;
}

int soma_lin(int *xs, size_t b, size_t e) {
    if (b == e) return 0;
    return xs[b] + soma_lin(xs, b+1, e);
}

// xs[b:e) válido e-b >= 2
// rearranja xs[b:e) de tal forma que
// xs[b:i) <= xs[i] < xs[i+1:e), para
// algum i em [b:e)
// devolve esse i
size_t partition(int *xs, size_t b, size_t e) {
    int x = xs[b];
    size_t i = b;
    for (size_t k = b + 1; k != e; ++k) {
        if (xs[k] <= x) {
            ++i;
            std::swap(xs[i], xs[k]);
        }
    }
    xs[b] = xs[i]; xs[i] = x;
    return i;
}

int *partition(int *begin, int *end) {
    int x = *begin;
    int *i = begin;
    for (int *k = std::next(begin); k != end; ++k) {
        if (*k <= x) {
            ++i;
            std::swap(*i, *k);
        }
    }
    *begin = *i; *i = x;
    return i;
}

void qsort(int *begin, int *end) {
    if (begin == end || std::next(begin) == end) return;
    int *i = partition(begin, end);
    qsort(begin, i);
    qsort(std::next(i), end);
}

void qsort(int *xs, size_t b, size_t e) {
    if (b == e || b+1 == e) return;
    size_t i = partition(xs, b, e);
    qsort(xs, b, i);
    qsort(xs, i+1, e);
}

void qsort_v2(int *xs, size_t b, size_t e) {
    while (true) {
        if (b == e || b+1 == e) return;
        size_t i = partition(xs, b, e);
        qsort_v2(xs, b, i);
        b = i + 1;
    }
}

int main() {
    int xs[] = {1, 4, 2, 0, 9, 5, 6, 3, 8, 7};
    qsort(std::begin(xs), std::end(xs));
    for (int x: xs) std::cout << x << ' '; 
}