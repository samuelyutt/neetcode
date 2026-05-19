class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> ret;
        int pi = -1, ni = -1;

        while (ret.size() < nums.size()) {
            pi++;
            while (nums[pi] < 0) {
                pi++;
            }
            ret.push_back(nums[pi]);

            ni++;
            while (nums[ni] > 0) {
                ni++;
            }
            ret.push_back(nums[ni]);
        }
        return ret;
    }
};