struct Node {
    int val;
    Node* next = nullptr;
};

// 0 -> 1 -> 2

class MyLinkedList {
public:
    Node* head = nullptr;
    int size = 0;

    MyLinkedList() {
        
    }

    Node* getNode(int index) {
        Node* node = head;
        for (int i = 0; i < index; i++) {
            node = node->next;
        }
        return node;
    }
    
    int get(int index) {
        if (index >= size) return -1;
        return getNode(index)->val;
    }
    
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    void addAtIndex(int index, int val) {
        if (index > size) return;

        Node* next = getNode(index);
        Node* node = new Node;
        node->val = val;

        if (next == head) {
            node->next = head;
            head = node;
        } else {
            Node* prev = getNode(index - 1);
            node->next = prev->next;
            prev->next = node;
        }

        size++;
    }
    
    void deleteAtIndex(int index) {
        if (index >= size) return;
        Node* node = getNode(index);

        if (node == head) {
            head = node->next;
        } else {
            Node* prev = getNode(index - 1);
            prev->next = node->next;
        }

        delete node;
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */