class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ret = 0, cur = 0;
        for (auto num : nums) {
            if (num == 1) {
                cur += 1;
            } else {
                cur = 0;
            }
            ret = max(ret, cur);
        }
        return ret;
    }
};