#include <iostream>
#include <iterator>
#include <utility>
#include <stack>


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

void qsort_it(int *xs, size_t b, size_t e) {
    std::stack<size_t> st;
    st.push(b); st.push(e);
    while (!st.empty()) {
        e = st.top(); st.pop();
        b = st.top(); st.pop();
        if (e - b <= 1) continue;
        size_t i = partition(xs, b, e);
        st.push(b); st.push(i);
        st.push(i+1); st.push(e);
    }   
}

void qsort_it(int *b, int *e) {
    std::stack<int *> st;
    st.push(b); st.push(e);
    while (!st.empty()) {
        e = st.top(); st.pop();
        b = st.top(); st.pop();
        if (e - b <= 1) continue;
        int *i = partition(b, e);
        st.push(b); st.push(i);
        st.push(i+1); st.push(e);
    }   
}


int main() {
    int xs[] {4,1,2,9,8,7,5,6,3,0};
    qsort_it (xs, 0, 10);
    for (int x: xs) std::cout << x << " ";
}