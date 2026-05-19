class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> pq;
        int ret = 0;
        for (int val : gifts) {
            pq.push(val);
            ret += val;
        }
        while (k--) {
            int valOld = pq.top();
            pq.pop();
            int valNew = (int)sqrt(valOld);
            pq.push(valNew);
            int diff = valOld - valNew;
            ret -= diff;
        }
        return ret;
    }
};