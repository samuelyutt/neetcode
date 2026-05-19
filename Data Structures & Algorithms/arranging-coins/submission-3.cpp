class Solution {
public:
    int arrangeCoins(int n) {
        int l = 0, r = n;
        while (l < r) {
            int m = (l + r + 1) / 2;
            long coins = (long) (1 + m) * m / 2;
            if (coins <= n) {
                l = m;
            } else {
                r = m - 1;
            }
        }
        return l;
    }
};