#include <iostream>
#include <iterator>

// using namespace std;

// begin != end && [begin:end] é válido && *[begin:end)está ordenado
// modifica *[begin:end] de tal forma que
//          *[begin:end] fique ordenado            

void insert(int *begin, int *end) {
    while (begin != end) {
        int *prev = std::prev(end); // end - 1
        if (*end < *prev) {
            int tmp = *end; *end = *prev; *prev = tmp;
            end = prev;
        }
        else break;
    }  
}

// [begin: end) é válido
// modifica *[begin:end) de tal forma que
//          *[begin:end) fique prdenado
void isort(int *begin, int *end) {
    // next(begin) == begin + 1
    for (int *p = std::next(begin); p != end; ++p)
        insert(begin, p);
}


int main() {
    int xs[] = {2, 7, 1, 3, 9, 4, 5, 6, 8};
    isort(std::begin(xs), std::end(xs));
    for (int x: xs) std::cout << x << ' ';
}