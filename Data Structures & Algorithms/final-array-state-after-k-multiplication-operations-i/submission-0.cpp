class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // min heap
        priority_queue<
            pair<int, int>,
            vector<std::pair<int, int>>,
            greater<std::pair<int, int>>
        > heap; // <num, idx>

        for (int i = 0; i < nums.size(); i++) {
            heap.push({nums[i], i});
        }

        // k operations
        while (k--) {
            auto pair = heap.top();
            heap.pop();
            heap.push({pair.first * multiplier, pair.second});
        }

        // build return value
        vector<int> ret;
        for (int i = 0; i < nums.size(); i++) {
            ret.push_back(0);
        }
        while (!heap.empty()) {
            auto pair = heap.top();
            heap.pop();
            ret[pair.second] = pair.first;
        }
        return ret;
    }
};