class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        deque<pair<int, int>> q;
        int m = grid.size();
        int n = grid.at(0).size();
        int ret = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    ret += 1;

                    // bfs
                    q.push_back({i, j});
                    while (!q.empty()) {
                        auto [x, y] = q.front();
                        q.pop_front();

                        if (x >= m || y >= n || x < 0 || y < 0)
                            continue;
                        if (grid[x][y] != '1')
                            continue;
                        grid[x][y] = '0';

                        q.push_back({x + 1, y});
                        q.push_back({x - 1, y});
                        q.push_back({x, y + 1});
                        q.push_back({x, y - 1});
                    }
                }
            }
        }
        return ret;
    }
};
