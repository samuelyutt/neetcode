class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int colorOri = image[sr][sc];
        int m = image.size();
        int n = image[0].size();
        deque<pair<int, int>> q = {{sr, sc}};
        while (!q.empty()) {
            auto pos = q.front();
            q.pop_front();
            int i = pos.first, j = pos.second;
            if (i >= m || j >= n || i < 0 || j < 0) {
                continue;
            }
            if (image[i][j] != colorOri) {
                continue;
            }
            if (image[i][j] == color) {
                continue;
            }
            image[i][j] = color;
            q.push_back({i + 1, j});
            q.push_back({i - 1, j});
            q.push_back({i, j + 1});
            q.push_back({i, j - 1});
        }
        return image;
    }
};