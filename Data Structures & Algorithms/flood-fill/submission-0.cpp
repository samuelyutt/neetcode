class Solution {
public:
    unordered_set<int> visited;
    int colorOri;

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        colorOri = image[sr][sc];
        traverse(sr, sc, image, sr, sc, color);
        return image;
    }

    void traverse(int i, int j, vector<vector<int>>& image, const int& sr, const int& sc, const int& color) {
        int m = image.size();
        int n = image[0].size();
        if (i >= m || j >= n || i < 0 || j < 0) {
            return;
        }
        if (visited.contains(i * n + j)) {
            return;
        }
        visited.insert(i * n + j);
        if (image[i][j] != colorOri){
            return;
        }
        image[i][j] = color;
        traverse(i - 1, j, image, sr, sc, color);
        traverse(i + 1, j, image, sr, sc, color);
        traverse(i, j - 1, image, sr, sc, color);
        traverse(i, j + 1, image, sr, sc, color);
    }
};