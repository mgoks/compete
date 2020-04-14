#include <iostream>
using namespace std;

#define uint64 unsigned long long

int pow(int x, int y) {
    int p = 1;
    while (y) {
        if (y&1) p *= x;
        x *= x;
        y >>= 1;
    }
    return p;
}
int main() {
    int T, a, b, n, k;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> a >> b >> n >> k;
        int count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i != j && (pow(i,a)%k + pow(j,b)%k) % k == 0){
                    count += 1;
                }
                count %= 1000000007;
            }
        }
        cout << "Case #" << t << ": " << count << endl;
    }
}