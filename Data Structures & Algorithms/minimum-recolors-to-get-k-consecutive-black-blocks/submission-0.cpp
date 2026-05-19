class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int l = 0, r = 0;
        int cnt = 0, ret = 101;
        for (int i = 0; i < k; i++) {
            if (blocks[r] == 'W') {
                cnt++;
            }
            r++;
        }
        while (r <= blocks.size()) {
            ret = min(cnt, ret);
            if (blocks[l] == 'W') {
                cnt--;
            }
            l++;
            if (blocks[r] == 'W') {
                cnt++;
            }
            r++;
        }
        return ret;
    }
};