#include <iostream>
#include <utility>
#include <stack>

using namespace std;

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

void qsort_it(int *xs, size_t b, size_t e) {
    stack<size_t> st;
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

void qsort_it(int *begin, int *end) {
    stack<int *> st;
    st.push(begin); st.push(end);
    while (!st.empty()) {
        end = st.top(); st.pop();
        begin = st.top(); st.pop();
        if (end - begin <= 1) continue;
        int *i = partition(begin, end);
        st.push(begin); st.push(i);
        st.push(i+1); st.push(end);

    }
}

int main() {
    int xs[] {4, 1, 2, 9, 8, 7, 5, 6, 3, 0};
    qsort_it(begin(xs), end(xs));
    for (int x: xs) cout << x << ' ';
}