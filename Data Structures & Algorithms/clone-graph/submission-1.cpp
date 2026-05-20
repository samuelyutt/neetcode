/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<int, pair<Node*, bool>> myNodes; // val -> [Node*, traversed]
    deque<Node*> q;

    Node* cloneGraph(Node* node) {
        if (node == nullptr) return node;

        // create my first node
        myNodes[node->val] = {new Node(node->val), false};

        // bfs
        q.push_back(node);
        while (!q.empty()) {
            Node* curNode = q.front();
            q.pop_front();
            traverse(curNode);
        }

        return myNodes[node->val].first;
    }

    void traverse(Node* node) {
        // assert node not visited
        bool& visited = myNodes[node->val].second;
        if (visited) return;
        visited = true;

        // assume my node is already created
        Node* myNode = myNodes[node->val].first;
        for (auto nei : node->neighbors) {
            // create my nei if not existed
            if (!myNodes.contains(nei->val)) {
                myNodes[nei->val] = {new Node(nei->val), false};
            }

            // add my nei to my node->neighbors
            myNode->neighbors.push_back(myNodes[nei->val].first);

            // add my nei to queue
            q.push_back(nei);
        }
    }
};
