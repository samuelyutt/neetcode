class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<vector<int>> dp;
        for (int j = 0; j < k; j++) {
            dp.push_back({});
        }

        for (int j = 0; j < k; j++) {
            for (int i = 0; i < nums.size() - j; i++) {
                if (j == 0) {
                    dp[j].push_back(nums[i]);
                } else {
                    dp[j].push_back(max(nums[i], dp[j - 1][i + 1]));
                }
            }
        }

        return dp.back();
    }
};
