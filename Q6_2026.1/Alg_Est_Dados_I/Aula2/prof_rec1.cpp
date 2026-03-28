#include <iostream>
#include <iterator>

// escreve [1:n]
void print(size_t n) {
    if (n == 0) return;
    print(n-1);
    std::cout << ' ' << n; 
}


// escreve [1:n]
void print2(size_t n) {
    if (n == 0) return;
    if (n == 1) {
        std::cout << ' ' << n;
        return;
    }
    print2(n-2);
    std::cout << ' ' << n-1 << ' ' << n; 
}

// escreve n, n-1, ..., 1
void printinv(size_t n) {
    if (n == 0) return;
    std::cout << ' ' << n;
    printinv(n-1);
}

// p[0:n) é válido
// devolve a soma dos elmts de p[0:n)
int soma(int *p, size_t n) {
    if (n == 0) return 0;
    return soma(p, n-1) + p[n-1];
}

// [begin:end) válido
// devolve a soma de *[begin:end)
int soma(int *begin, int *end) {
    if (begin == end) return 0;
    return soma(begin, end-1) + end[-1];
}

// [begin:end) válido
// devolve a soma de *[begin:end)
int soma2(int *begin, int *end) {
    if (begin == end) return 0;
    return *begin + soma2(begin + 1, end);
}


int main() {
    int v[] {1, 4, 5, 2, 4, 7};
    std::cout << soma2(std::begin(v), std::end(v));
}