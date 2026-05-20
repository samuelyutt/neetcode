class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> store; // key -> vector of <value, timestamp>

    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if (!store.contains(key)) {
            // create the entry
            store[key] = {};
        }
        // append the value and timestamp
        store[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        // check if in store
        if (!store.contains(key)) {
            return "";
        }
        // check if the latest one is availeble
        if (store[key].front().second > timestamp) {
            return "";
        }

        // binary search for timestamp
        // find the one with max ts smaller than curr timestamp
        // 1 3 5 -> 4
        auto& v = store[key];
        int l = 0, r = v.size() - 1;
        while (l < r) {
            int m = (l + r + 1) / 2;
            if (v[m].second > timestamp) {
                r = m - 1;
            } else {
                l = m;
            }
        }
        return v[l].first;
    }
};
