class Solution {
public:
    vector<vector<int>>* img;
    int newColor, oriColor;
    int m, n;

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        img = &image;
        newColor = color;
        oriColor = image[sr][sc];
        m = image.size();
        n = image[0].size();
        traverse(sr, sc);
        return image;
    }

    void traverse(int i, int j) {
        if (i >= m || j >= n || i < 0 || j < 0) {
            return;
        }
        if ((*img)[i][j] != oriColor){
            return;
        }
        if ((*img)[i][j] == newColor){
            return;
        }
        (*img)[i][j] = newColor;
        traverse(i - 1, j);
        traverse(i + 1, j);
        traverse(i, j - 1);
        traverse(i, j + 1);
    }
};