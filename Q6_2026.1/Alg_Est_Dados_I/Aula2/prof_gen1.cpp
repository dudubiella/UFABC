#include <iostream>
#include <iterator>
#include <utility>
#include <vector>
#include <array>
#include <forward_list>

// using namespace std;

// begin != end && [begin:end] é válido && *[begin:end)está ordenado
// modifica *[begin:end] de tal forma que
//          *[begin:end] fique ordenado            
template <typename I>
void insert(I begin, I end) {
    while (begin != end) {
        I prev = std::prev(end); // end - 1
        if (*end < *prev) {
            std::swap(*end, *prev);
            end = prev;
        }
        else break;
    }  
}

// [begin: end) é válido
// modifica *[begin:end) de tal forma que
//          *[begin:end) fique prdenado
template <typename I>
void isort(I begin, I end) {
    for (I p = std::next(begin); p != end; ++p)
        insert(begin, p);
}

template <typename I>
void prn(I begin, I end) {
    while (begin != end) {
        std::cout << *begin << ' ';
        ++begin;
    }
    std::cout << '\n';
}
 

int main() {
    int xs[] {2, 7, 1, 3, 9, 4, 5, 6, 8};
    char cs[] {'a', 'u', 'b', 'c'};
    std::vector<int> vs {1, 5, 2, 3, 9, 7, 6, 4};
    isort(std::begin(xs), std::end(xs));
    isort(std::begin(cs), std::end(cs));
    prn(std::begin(xs), std::end(xs));
    prn(std::begin(cs), std::end(cs));
    isort(std::begin(vs), std::end(vs));
    prn(std::begin(vs), std::end(vs));
    std::array as {1, 4, 8, 9, 2, 7};
    isort(std::begin(as), std::end(as));
    prn(std::begin(as), std::end(as));
    std::forward_list ls {4, 1, 2, 3, 7};
    prn(std::begin(ls), std::end(ls));
}