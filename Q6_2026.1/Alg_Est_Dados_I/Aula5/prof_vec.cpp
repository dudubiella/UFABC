#include <iostream>
#include <vector>
#include <utility>
#include <cassert>

using namespace std;

class vec {
private:
    size_t capacity;
    size_t sz;
    int *elems;
public:
    vec(size_t max_cap = 10) {
        capacity = max((size_t) 10, max_cap);
        sz = 0;
        elems = new int[capacity];
    }

    ~vec() {
        delete[] elems;
    }

    void push_back(int x) {
        if (sz == capacity) {
            capacity = max((size_t) 10, 2 * capacity);
            int *new_elems = new int[capacity];
            int *q = new_elems;
            for (int *p = elems; p != elems + sz;) 
                *q++ = *p++;
            delete[] elems;
            elems = new_elems;
        }
        elems[sz++] = x;
    }

    int at(size_t i) {
        assert(i < sz);
        return elems[i];
    }

    int& operator[](size_t i) {
        return elems[i];
    }

    void pop_back() {
        assert(sz >= 0);
        --sz;
        if (sz == capacity/4) {
            capacity = max((size_t) 10, capacity/2);
            int *new_elems = new int[capacity];
            int *q = new_elems;
            for (int *p = elems; p != elems + sz;)
                *q++ = *p++;
            delete[] elems;
            elems = new_elems;
        }
    }

    int& back() { return elems[sz-1]; }

    size_t size() { return sz; }

};

int main() {
    vec v(20);
    for (int i = 0; i < 100; ++i)
        v.push_back(i);
    for (int i = 0; i < v.size(); ++i) {
        v[i] += 40;
    }    
    for (size_t i = 0; i < v.size(); ++i) 
        cout << v[i] << ' ';
    
   
}
