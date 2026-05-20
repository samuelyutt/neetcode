class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> ret;
        int j = 0;
        for (auto ab : firstList) {
            int a = ab[0], b = ab[1];
            while (j < secondList.size() && secondList[j][0] <= b) {
                int x = secondList[j][0], y = secondList[j][1];
                if (y >= a) {
                    ret.push_back({
                        max(a, x),
                        min(b, y)
                    });
                }
                if (y > b) {
                    break;
                }
                j++;
            }
        }
        return ret;
    }
};