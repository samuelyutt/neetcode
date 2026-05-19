class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int>> v;
        for (char c : s) {
            if (!v.empty() && v.back().first == c) {
                auto &back = v.back();
                back.second++;
                if (back.second == k) {
                    v.pop_back();
                }
            } else {
                v.push_back({c, 1});
            }
        }
        string ret;
        for (auto p : v) {
            for (int i = 0; i < p.second; i++) {
                ret += p.first;
            }
        }
        return ret;
    }
};