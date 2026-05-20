struct Node {
    int key;
    int val;
    Node* prev = nullptr;
    Node* next = nullptr;
};

class LRUCache {
public:
    unordered_map<int, Node*> m;
    Node* head = nullptr;
    Node* tail = nullptr;
    int cap;

    LRUCache(int capacity) {
        cap = capacity;
    }

    void use(Node* node) {
        if (node == tail) return;

        // detatch node
        if (node->prev) {
            node->prev->next = node->next;
        }
        if (node->next) {
            node->next->prev = node->prev;
        }

        // update head (if needed)
        if (node == head) {
            head = node->next;
        }

        // move to tail
        tail->next = node;
        node->prev = tail;
        node->next = nullptr;
        tail = node;
    }
    
    int get(int key) {
        if (!m.contains(key)) return -1;
        Node* node = m[key];
        use(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (!m.contains(key)) {
            // new node inserted
            Node* node = new Node;
            node->key = key;
            node->val = value;
            m[key] = node;

            // add this node to tail
            if (head == nullptr) {
                head = node;
                tail = node;
            } else {
                tail->next = node;
                node->prev = tail;
                node->next = nullptr;
                tail = node;
            }

            // remove LRU if reach capacity
            if (m.size() > cap) {
                Node* nodeRm = head;
                head = head->next;
                head->prev = nullptr;
                m.erase(nodeRm->key);
                delete nodeRm;
            }
        } else {
            Node* node = m[key];
            node->val = value;
            use(node);
        }
    }
};
