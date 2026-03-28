#include <iostream>
#include <vector>
#include <stack>

using namespace std;

using graph = vector<vector<int>>;

void foo(int& x) {
    ++x;
}

void foop(int *p) {
    (*p)++;
}

vector<int> dfs(graph& G, int s) {
    stack<int> st;
    vector<int> pred(G.size(), -1);
    pred[s] = s;
    st.push(s);
    while (!st.empty()) {
        int x = st.top();
        int i;
        for (i = 0; i < G[x].size() && pred[G[x][i]] != -1; ++i);
        if (i == G[x].size()) {
            // todos os vizinhos já foram marcados
            st.pop();
        }
        else {
            int y = G[x][i];
            st.push(y);
            pred[y] = x;
        }
    }
    return pred;
}

vector<int> dfs_curr(graph& G, int s) {
    stack<int> st;
    vector<int> pred(G.size(), -1);
    vector<size_t> curr(G. size(), 0);
    pred[s] = s;
    st.push(s);
    while (!st.empty()) {
        int x = st.top();
        if (curr[x] == G[x].size()) {
            st.pop();
            continue;
        }
        int y = G[x][curr[x]];
        if (pred[y] == -1) { 
            pred[y] = x;
            st.push(y);
        }
        ++curr[x];
        
    }
    return pred;
}

vector<int> dfs_curr_it(graph& G, int s) {
    stack<int> st;
    vector<int> pred(G.size(), -1);
    vector<vector<int>::iterator> curr(G. size());
    for (size_t i = 0; i < G.size(); ++i) 
        curr[i] = begin(G[i]);
    pred[s] = s;
    st.push(s);
    while (!st.empty()) {
        int x = st.top();
        if (curr[x] == end(G[x])) {
            st.pop();
            continue;
        }
        int y = *curr[x];
        if (pred[y] == -1) { 
            pred[y] = x;
            st.push(y);
        }
        ++curr[x];
        
    }
    return pred;
}

vector<int> dfs_curr_it_2(graph& G, int s) {
    stack<pair<int, vector<int>::iterator>> st;
    vector<int> pred(G.size(), -1);
    pred[s] = s;
    st.push({s, begin(G[s])});
    while (!st.empty()) {
        auto &[x, it] = st.top();
        if (it == end(G[x])) {
            st.pop();
            continue;
        }
        int y = *it;
        if (pred[y] == -1) { 
            pred[y] = x;
            st.push({y, begin(G[y])});
        }
        ++it;
    }
    return pred;
}




int main() {
    graph G { {1, 2}, {0, 7, 8}, {3, 0}, {4, 2, 5},
    {3, 5}, {3, 4, 6}, {5}, {1, 8}, {1, 7}, 
    {10}, {9, 11}, {10}};

    vector<int> p = dfs_curr_it_2(G, 0);
    for (int x: p) cout << x << ' ';
}