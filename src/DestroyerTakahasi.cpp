#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ii = pair<ll, ll>;

int main() {
    ios::sync_with_stdio(false);
    int N;
    ll D;
    cin >> N >> D;

    vector<ii> xs(N);

    for (auto& [R, L] : xs)
        cin >> L >> R;
    
    // Ordena os intervalos por em uma heap
    priority_queue<ii, vector<ii>, greater<ii>> pq(xs.begin(), xs.end());

    auto res = 0;

    while (not pq.empty()) {
        // Pega o intervalo com menor valor
        auto [b, a] = pq.top();
        pq.pop();
        auto c = b + D - 1;

        // Identifica os intevalos conflitantes e os remove
        while (not pq.empty() and pq.top().second <= c)
            pq.pop();

        // Incrementa o resultado
        ++res;
    }

    cout << res << "\n";
    return 0;
}
