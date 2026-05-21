struct Node {
    int key;
    int val;
    Node* prev = nullptr;
    Node* next = nullptr;
};

class LRUCache {
public:
    // cap >= 1
    int cap;

    // double linked list: O(1) insersion
    Node* head = nullptr;
    Node* tail = nullptr;

    // hash map: O(1) look up
    unordered_map<int, Node*> m; // key -> Node

    LRUCache(int capacity) {
        cap = capacity;
    }

    // remove from list and map
    void remove(Node* node) {
        // detatch from linked list
        if (node->prev)
            node->prev->next = node->next;
        if (node->next)
            node->next->prev = node->prev;

        // update head and tail
        if (node == head)
            head = node->next;

        if (node == tail)
            tail = node->prev;

        // clear node pointers
        node->prev = nullptr;
        node->next = nullptr;

        // remove from map
        m.erase(node->key);
    }

    // insert to list and map
    void insert(Node* node) {
        if (!head) {
            // insert the first node
            head = tail = node;
        } else {
            // attach to the tail
            node->prev = tail;
            node->next = nullptr;
            tail->next = node;
            tail = node;
        }

        // add/update map
        m[node->key] = node;

        // remove head node if exceed cap
        if (m.size() > cap) {
            Node* lru = head;
            remove(lru);
            delete lru;
        }
    }
    
    int get(int key) {
        if (!m.contains(key))
            return -1;
        
        Node* node = m[key];
        remove(node);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {
        Node* node;
    
        if (!m.contains(key)) {
            // create a new node for new key
            node = new Node;
            node->key = key;
            node->val = value;
        } else {
            // retrieve the node and update its value
            node = m[key];
            node->val = value;
            remove(node);
        }

        insert(node);
    }
};
