class Solution {
public:
    int m, n;

    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid.at(0).size();

        int ret = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    ret += 1;
                    dfs(i, j, grid);
                }
            }
        }
        return ret;
    }

    void dfs(int i, int j, vector<vector<char>>& grid) {
        if (i >= m || j >= n || i < 0 || j < 0) {
            return;
        }
        if (grid[i][j] != '1') {
            return;
        }
        grid[i][j] = '2';
        dfs(i + 1, j, grid);
        dfs(i - 1, j, grid);
        dfs(i, j + 1, grid);
        dfs(i, j - 1, grid);
    }
};
