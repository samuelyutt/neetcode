class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for (auto num : nums) {
            s.insert(num);
        }

        int ret = 0;
        deque<int> q;
        while (!s.empty()) {
            int val = *s.begin();
            s.erase(val);
            q.push_back(val);

            int cnt = 0;
            while (!q.empty()) {
                val = q.front();
                q.pop_front();

                cnt++;
                ret = max(ret, cnt);

                if (s.contains(val - 1)) {
                    s.erase(val - 1);
                    q.push_back(val - 1);
                }
                if (s.contains(val + 1)) {
                    s.erase(val + 1);
                    q.push_back(val + 1);
                }
            }
        }
        return ret;
    }
};
