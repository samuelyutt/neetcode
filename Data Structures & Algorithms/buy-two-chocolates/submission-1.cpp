class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int a = min(prices[0], prices[1]);
        int b = max(prices[0], prices[1]);
        for (int i = 2; i < prices.size(); i++) {
            int p = prices[i];
            if (p <= a) {
                b = a;
                a = p;
            } else if (p <= b) {
                b = p;
            }
        }
        if ((a + b) <= money) {
            money -= (a + b);
        }
        return money;
    }
};