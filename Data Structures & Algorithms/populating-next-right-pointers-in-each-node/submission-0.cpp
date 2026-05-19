/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        vector<Node*> v = {root};

        while (1) {
            if (v.front() == nullptr) {
                break;
            }

            Node* prev = nullptr;
            for (auto it = v.end() - 1; it >= v.begin(); it--) {
                Node* node = *it;
                node->next = prev;
                prev = node;
            }

            vector<Node*> vNew;
            for (auto node : v) {
                vNew.push_back(node->left);
                vNew.push_back(node->right);
            }
            v = vNew;
        }
        return root;
    }
};