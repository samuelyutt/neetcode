class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m; // num -> cnt
        for (auto num : nums) {
            if (m.contains(num)) {
                m[num]++;
            } else {
                m[num] = 1;
            }
        }

        priority_queue<pair<int, int>> pq;
        for (auto [num, cnt] : m) {
            pq.push({cnt, num});
        }

        vector<int> ret;
        while(k--) {
            auto [cnt, num] = pq.top();
            pq.pop();
            ret.push_back(num);
        }
        return ret;
    }
};
