#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define foreach(i,x) for(type(x)i = x.begin(); i != x.end(); i++)
#define FOR(ii, aa, bb) for(int ii = aa; ii <= bb; ii++)
#define type(x) __typeof(x.begin())

typedef long long ll;

const int mod = (int) 1e9 + 7;
const int N = 2e5 + 5;

int n, m, x, y, dp[N][11][11], temp[N][11][11];
vector<int> v[N];

void dfs(int node, int root) {
    dp[node][0][0] = 1;
    foreach(it, v[node]) {
        if(*it == root) continue;
        dfs(*it, node);
        FOR(i, 0, 10){
            FOR(j, 0, 10) {
                temp[node][i][j] = dp[node][i][j];
                dp[node][i][j] = 0;
            }
        }
        FOR(i, 0, m){
            FOR(j, 0, m - i){
                FOR(k, 0, m){
                    dp[node][i + j][k] = (dp[node][i + j][k] + temp[node][i][k] * (ll) dp[*it][j][0]) % mod;
                    dp[node][i + j][k + 1] = (dp[node][i + j][k + 1] + temp[node][i][k] * (ll) dp[*it][j][1]) % mod;
                    if(k) dp[node][i + j + 1][k - 1] = (dp[node][i + j + 1][k - 1] + temp[node][i][k] * (ll) dp[*it][j][1] % mod * k) % mod;
                    dp[node][i + j + 1][k] = (dp[node][i + j + 1][k] + temp[node][i][k] * (ll) dp[*it][j][1] % mod) % mod;
                }
            }
        }
    }   
    FOR(i, 0, m) dp[node][i][1] = (dp[node][i][1] + dp[node][i][0]) % mod;
}

int main() {
    cin >> n >> m;
    FOR(i, 2, n) {
        cin >> x >> y;
        v[x].pb(y);
        v[y].pb(x);
    }
    dfs(1, 0);
    cout << dp[1][m][0] << endl;
    return 0;
}
