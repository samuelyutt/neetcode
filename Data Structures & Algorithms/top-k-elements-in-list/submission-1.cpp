class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m; // <num, cnt>
        for (auto num : nums) {
            if (!m.contains(num)) {
                m[num] = 0;
            }
            m[num]++;
        }

        priority_queue<pair<int, int>> pq; // <cnt, num>
        for (auto pair : m) {
            pq.push({pair.second, pair.first});
        }

        vector<int> ret;
        while (k--) {
            ret.push_back(pq.top().second);
            pq.pop();
        }
        return ret;
    }
};
