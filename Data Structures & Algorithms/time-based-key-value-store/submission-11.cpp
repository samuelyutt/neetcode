class TimeMap {
public:
    // key -> vector of <value, timestamp>
    unordered_map<string, vector<pair<string, int>>> store;

    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        
        // create the entry if not exist
        if (!store.contains(key)) {
            store[key] = {};
        }

        // append the value and timestamp
        store[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        // check if exist
        if (!store.contains(key)) {
            return "";
        }

        // check if the first one is availeble
        if (store[key].front().second > timestamp) {
            return "";
        }

        // binary search for timestamp
        // find the one with max ts smaller than curr timestamp
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
