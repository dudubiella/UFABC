#include <iostream>
#include <iterator>
#include <utility>



// entrada [comeco:fim] é valido && comeco != fim && *[comeco:fim) está ordenado
// modifica *[comeco:fim] de tal forma que *[comeco:fim] fique ordenado

template <typename I>
void insert (I comeco, I fim) {
    //I::value_type x = *fim;
    auto x = *fim;
    while (comeco != fim && x < *(fim - 1)) {
        *fim = *(fim - 1);
        --fim;
    }
    *fim = x;
}

template <typename I>
void isort(I comeco, I fim){
    for (I p = comeco + 1; p < fim; ++p){
        insert (comeco, p);
    }
}

template <typename I>
void imprime(I comeco, I fim){
    while (comeco != fim){
        std::cout << *comeco << ' ';
        ++comeco;
    }
    std::cout << '\n';
}

int main(){
    int v[] = {4,3,0,5,1,7,9,8};
    isort(std::begin(v), std::end(v));
    imprime (std::begin(v), std::end(v));
    char s[] = {'d', 'c', 'a', 'b'};
    isort(std::begin(s), std::end(s));
    imprime (std::begin(s), std::end(s));
}