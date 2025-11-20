#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);

    int t, x, y, k;
    cin >> t;
    for (; t--;) {
        cin >> x >> y >> k;
        vector<long long> a(n);
        long long x = 0;

        for (int i = 0; i < n; i++) {
            cin >> a[i];
            x += a[i];
        }

        long long _m = 0;

        for (int i = 0; i < n; i++) {
            long long nx = 0;
            for (int j = i; j < n; j++) {
                nx -= a[j];
                long long len = j - i + 1;
                _m = max(_m, len * ((i + 1) + (j + 1)) + nx);
            }
        }

        cout << _m + x << "\n";
    }
    return 0;
}
