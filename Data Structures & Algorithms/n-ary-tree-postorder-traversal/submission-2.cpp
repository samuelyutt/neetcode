/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> ret;

    void traverse(Node* node) {
        for (auto child : node->children) {
            traverse(child);
        }
        ret.push_back(node->val);
    }

    vector<int> postorder(Node* root) {
        if (root == nullptr) {
            return {};
        }
        traverse(root);
        return ret;
    }
};