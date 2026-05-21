class BrowserHistory {
public:
    vector<string> hist;
    int idx;

    BrowserHistory(string homepage) {
        hist.push_back(homepage);
        idx = 0;
    }
    
    void visit(string url) {
        // clear all the forward history
        while (hist.size() > idx + 1)
            hist.pop_back();

        // visit
        hist.push_back(url);
        idx++;
    }
    
    string back(int steps) {
        idx = max(0, idx - steps);
        return hist[idx];
    }
    
    string forward(int steps) {
        idx = min((int)hist.size() - 1, idx + steps);
        return hist[idx];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */