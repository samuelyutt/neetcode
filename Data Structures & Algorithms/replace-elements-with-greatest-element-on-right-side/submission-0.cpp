class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int cur = -1;
        for (int i = arr.size() - 1; i >= 0; i--) {
            int ori = arr[i];
            arr[i] = cur;
            if (ori > cur) {
                cur = ori;
            }
        }
        return arr;
    }
};