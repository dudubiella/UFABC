#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class int_queue {
private:
    size_t cap;
    size_t begin;
    size_t sz;

    int *elems;

public:
    int_queue(size_t c){
        cap = c;
        elems = new int[c];
        begin = 0;
        sz = 0;
    }

    ~int_queue(){
        delete [] elems;
    }

    void push(int x) {
        assert(sz < cap);
        elems[(begin + sz) % cap] = x;
        ++sz;
    }

    int front() {
        assert(sz > 0);
        return elems[begin];
    }

    void pop() {
        assert(sz > 0);
        begin = (begin + 1) % cap;
        --sz;
    }

    bool empty() {
        return sz == 0;
    }

    size_t size() {
        return sz;
    }
};

struct node {
    int info;
    node *next;
    node (int i, node *n = nullptr) {info = i; next = n;}
};

class int_ll_queue {
private:
    node *begin, *end;
public:
    int_ll_queue() {
        begin = end = nullptr;
    }

    ~int_ll_queue() {
        while (begin != nullptr) {
            node *aux = begin;
            begin = begin->next;
            delete aux;
        }
    }

    void push(int x) {
        if (end == nullptr) {
            begin = end = new node(x);
        } 
        else {
            end = end->next = new node(x);
        }
    }

    void pop() {
        assert(begin != nullptr);
        node *bn = begin->next;
        delete begin;
        begin = bn;
        if (begin == nullptr) end = nullptr;
    }

    int front() {
        assert(begin != nullptr);
        return begin->info;
    }

    bool empty() { return begin == nullptr; }
};

using graph = vector<vector<int>>;

vector<int> bfs(graph &G, int s){
    int_queue q(G.size());
    q.push(s);
    vector<int> pred(G.size(), -1);
    pred[s] = s;
    while (!q.empty()){
        int x = q.front();
        q.pop();
        for (int y : G[x]){
            if (pred[y] == -1){
                pred[y] = x;
                q.push(y);
            }
        }
    }
    return pred;
}

int main() {
    graph G {
        {1, 2, 3},
        {0, 2, 3, 4},
        {0, 1, 4},
        {1, 5},
        {1, 2, 5, 6},
        {3, 4, 7},
        {4, 7},
        {5, 6}
    };
    auto p = bfs(G, 0);
    for (size_t i = 0; i < p.size(); ++i) {
        cout << "pred[" << i << "] = " << p[i] << '\n';
    }
}