class Solution {
public:

    string encode(vector<string>& strs) {
        string ret = "";
        for (auto s : strs) {
            ret += to_string(s.length());
            ret += "|";
            ret += s;
        }
        return ret;
    }

    vector<string> decode(string s) {
        vector<string> ret;
        int i = 0;

        while (i < s.length()) {
            string buff = "";
            while (s[i] != '|') {
                buff += s[i];
                i++;
            }
            i++;

            int len = std::stoi(buff);
            buff = "";
            while (len--) {
                buff += s[i];
                i++;
            }
            
            ret.push_back(buff);
        }

        return ret;
        
    }
};
