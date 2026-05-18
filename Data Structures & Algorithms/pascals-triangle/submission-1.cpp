class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ret = {{1}};

        for (int i = 1; i < numRows; i++) {
            // vector<int> prev = ret.back(); // This creates a copy of the last vector.
            const vector<int>& prev = ret.back(); // a reference (no copy)

            vector<int> cur = {1};
            for (int j = 0; j < prev.size() - 1; j++) {
                cur.push_back(prev[j] + prev[j + 1]);
            }
            cur.push_back(1);
            ret.push_back(cur);
        }

        return ret;
    }
};