#include <iostream>
#include <cassert>
#include <iterator>

using namespace std;

// entrada: [begin: end) é válida E begin != end
// saída: um apontador para um menor elemento de *[begin: end)

int *min_elment(int *begin, int *end) {
    assert(begin != end);
    int *m = begin;
    ++begin;
    while (begin != end) {
        if (*begin < *m) m = begin;
        ++begin;
    }
    return m;
}

// entrada: [begin: end) válida
// modifica: rearranja *[begin:end) de tal for que
//           *p <= *(p+1) para cada p em [begin:end-1)
void selsort(int *begin, int *end) {
    for (int *s = begin; s != end; ++s) {
        int *m = min_elment(s, end);
        int tmp = *m; *m = *s; *s = tmp;
    }
}


// entrada: [begin: end) é válido
// saída: soma dos elementos de *[begin: end)
// consumo de tempo: O(n), onde n = dist(begin, end)
int soma(int *begin, int *end) {
    int s = 0;
    for (int *p = begin; p != end; ++p) {
        s += *p;
    }
    return s;
}

// entrada: p[0:n) é válido 
// saída: a soma dos elmentos de p[0:n)
// consumo de tempo: O(n)
int soma(int *p, size_t n) {
    int s = 0;
    for (size_t i = 0; i < n; ++i)
        s += p[i];
    return s;
}

int main() {
    int xs[] = {1, 2, 4, 8, 3, 9, 2, 5, 7};
    selsort(begin(xs), end(xs));
    for (int x: xs) cout << x << ' ';
}

