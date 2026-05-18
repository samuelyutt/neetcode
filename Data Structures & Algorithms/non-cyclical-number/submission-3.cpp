class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> s;
        while (n != 1) {
            if (s.contains(n)) {
                return false;
            }
            s.insert(n);
            n = replace(n);
        }
        return true;
    }

    int replace(int n) {
        int ret = 0;
        while (n) {
            int val = n % 10;
            n /= 10;
            ret += pow(val, 2);
        }
        return ret;
    }
};
