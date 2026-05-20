class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // min heap
        priority_queue<
            pair<int, int>,
            vector<std::pair<int, int>>,
            greater<std::pair<int, int>>
        > heap; // min heap of <num, idx>

        for (int i = 0; i < nums.size(); i++) {
            heap.push({nums[i], i});
        }

        // k operations
        while (k--) {
            auto [num, idx] = heap.top();
            heap.pop();
            heap.push({num * multiplier, idx});
        }

        // build return value
        vector<int> ret(nums.size());
        while (!heap.empty()) {
            auto [num, idx] = heap.top();
            heap.pop();
            ret[idx] = num;
        }
        return ret;
    }
};