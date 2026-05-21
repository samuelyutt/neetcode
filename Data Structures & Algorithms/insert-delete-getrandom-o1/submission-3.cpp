class RandomizedSet {
public:
    vector<int> v; // val
    unordered_map<int, int> m; // val -> idx

    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (m.contains(val))
            return false;
        int idx = v.size();
        m[val] = idx;
        v.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (!m.contains(val))
            return false;
        int idx = m[val];
        v[idx] = v[v.size() - 1];
        m[v[v.size() - 1]] = idx;
        v.pop_back();
        m.erase(val);
        return true;
    }
    
    int getRandom() {
        return v[rand() % v.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */