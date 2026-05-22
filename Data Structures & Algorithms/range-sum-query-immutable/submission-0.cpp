class NumArray {
public:
    vector<int> sums = {0};

    NumArray(vector<int>& nums) {
        int s = 0;
        for (int num : nums) {
            s += num;
            sums.push_back(s);
        }
    }
    
    int sumRange(int left, int right) {
        return sums[right + 1] - sums[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */