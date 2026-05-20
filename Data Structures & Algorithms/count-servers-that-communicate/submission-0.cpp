class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid.at(0).size();
        vector<int> rCnt(m);
        vector<int> cCnt(n);

        // first scan: counts appearance of rows and cols
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    rCnt[i]++;
                    cCnt[j]++;
                }
            }
        }

        // second scan: count number of servers that can communicate
        int ret = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    if (rCnt[i] > 1 || cCnt[j] > 1) {
                        ret++;
                    }
                }
            }
        }
        return ret;
    }
};