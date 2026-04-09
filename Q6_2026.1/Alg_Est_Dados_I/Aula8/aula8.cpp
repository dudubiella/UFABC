#include <iostream>
#include <utility>

using namespace std;

struct tnode {
    int info;
    tnode *left;
    tnode *right;

    tnode(int i, tnode *l = nullptr, tnode *r = nullptr) {
        info = i;
        left = l;
        right = r;
    }
};

//recebe [b:e) valido
//devolve a raiz de uma AB (arvore binária) com os elementos de [b:e)
tnode *make_bt(int *b, int *e) {
    auto n = e - b;
    if (n == 0) return nullptr;
    auto m = b + n/2;
    return new tnode(*m, make_bt(b, m), make_bt(m + 1, e));
}

void print_bt(tnode *t, int tab = 0) {
    if (t == nullptr) return;
    print_bt(t->left, tab + 4);
    for (int i = 0; i < tab; ++i) cout << ' ';
    cout << t->info << '\n';
    print_bt(t->right, tab + 4);
}

size_t count(tnode *t) {
    return  t == nullptr
            ? 0 
            : 1 + count(t->left) + count(t->right);
}

size_t ct_alm_leaves(tnode *t) {
    if (t == nullptr) return 0;
    if (t->left == nullptr && t->right == nullptr) return 1;
    return ct_alm_leaves(t->left) + ct_alm_leaves(t->right);
}

size_t count_leaves(tnode *t) {
    if (t == nullptr) return 0;
    if (t->left == nullptr && t->right == nullptr) return 0;
    return ct_alm_leaves(t);
}

size_t leaves(tnode *t, bool is_root = true) {
    if (t == nullptr) return 0;
    if (t->left == nullptr && t->right == nullptr) return is_root ? 0 : 1;
    return leaves(t->left, false) + leaves(t->right, false);
}

// t != nullptr
size_t height_0(tnode *t) {
    if (t->left == nullptr && t->right == nullptr) return 0;
    size_t hl = 0;
    if (t->left) hl = height_0(t->left);
    size_t hr = 0;
    if (t->right) hr = height_0(t->right);
    return 1 + max(hl, hr);
}

int height(tnode *t) {
    return t == nullptr ? -1 : 1 + max(height(t->left), height(t->right));
}

size_t el_in_lv(tnode *t, int lv, int atual = 0) {
    if (t == nullptr) return 0;
    if (lv == atual) return 1;
    return el_in_lv(t->left, lv, atual + 1) + el_in_lv(t->right, lv, atual + 1);
}

// [b:b+count(t)) é valido
int *to_vec(tnode *t, int *b) {
    if (t == nullptr) return b;
    int *e = to_vec(t->left, b);
    *e = t->info;
    return to_vec(t->right, e + 1);
}

int main() {
    int xs[] = {2, 5, 7, 9, 11, 15, 20, 22};
    tnode *t = make_bt(xs, xs + 8);
    print_bt(t);
    cout << "count = " << count(t) << '\n';
    int ys[10];
    int *e = to_vec(t, ys);
    for (int *b = ys; b < e; ++b) {
        cout << *b << ' ';
    }
    cout << '\n';
    cout << "leaves = " << leaves(t) << '\n';
    cout << "count_leaves = " << count_leaves(t) << '\n';
    cout << "height_0 = " << height_0(t) << '\n';
    cout << "height = " << height(t) << '\n';

}