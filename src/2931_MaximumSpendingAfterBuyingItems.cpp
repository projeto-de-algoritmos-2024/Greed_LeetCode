class Solution {
    using ll = long long;

public:
    ll maxSpending(vector<vector<int>>& values) {
        ios::sync_with_stdio(false);

        int n = values.size(), m = values[0].size();

        // Ordena pelo preco de forma crescente
        vector<int> temp;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                temp.push_back(values[i][j]);

        sort(temp.begin(), temp.end());

        // Calcula o valor maximo
        ll res = 0;

        int c = m * n;

        for (int i = 1; i <= c; i++)
            res += (ll)i * temp[i - 1];

        return res;
    }
};