#include <iostream>
#include <cassert>
#include <iterator>

using namespace std;

//Anotações: 

//  using namespace std;
//  para evitas escrever sempre:
//  std::cout << "imprime" << '\n'

//  size_t
//  substitui o tipo que pode depender

//  #include <iterator>
//  permite evitar escrever sempre (p, p + tam) virando (begin (p), end(p)) 



// entrada: p[0:n) é valido
// saída: a soma dos elementos de p[0:n)

int soma (int *p, size_t tamanho) {
    int soma = 0;

    for (size_t i = 0; i < tamanho; ++i) {
        soma += p [i];
    }
    return soma;
}

// entrada: p[comeco:final) é valido
// saída: a soma dos elementos de *[comeco:final)
// Consumo de tempo: O(n), onde n é a distância de tempo, n = d(comeco, final)

int soma (int *comeco, int *final) {
    int soma = 0;
    for (int *p = comeco; p != final; ++p) {
        soma += *p;
    }
    return soma;
}

// entrada: [comeco:final) é valida && comeco != final
// saida: um apontador para um menor elemento de *[comeco:final)
// Consumo de tempo:

int *min_elemento (int *comeco, int *final) {
    assert (comeco != final && comeco < final);
    int *min = comeco++;
    while (comeco != final) {
        if (*comeco < *min) min = comeco;
        comeco ++;
    }
    return min;
}

// entrada: [comeco:final) é valida
// Modifica: rearanja *[comeco:final) de tal forma que
//           *p <= *(p + 1) para cada p em *[comeco:final - 1)
// Consumo de tempo:

void selsort (int *comeco, int *final) {
    for (int *p = comeco; p != final; ++p) {
        int *m = min_elemento (p, final);
        int temp = *m; *m = *p; *p = temp;
    }
}

int main () {
    int n = 10;
    int xs[n] = {1,2,3,9,7,56,23,12,-3,52};

    cout << soma (xs, n) << '\n';

    cout << soma (xs + 2, xs + 6) << '\n';

    cout << *min_elemento(xs, xs + 10) << '\n';

    selsort (xs, xs + 10);
//    selsort (begin(xs), end(xs));
    for (int x: xs) cout << x << ' ';

    return 0;
}