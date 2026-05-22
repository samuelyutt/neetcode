/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    stack<int> parse(ListNode* node) {
        stack<int> s;
        while (node) {
            s.push(node->val);
            node = node->next;
        }
        return s;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1 = parse(l1);
        stack<int> s2 = parse(l2);
        int carry = 0;
        ListNode* next = nullptr;

        while (!s1.empty() || !s2.empty()) {
            int num = carry;
            if (!s1.empty()) {
                num += s1.top();
                s1.pop();
            }
            if (!s2.empty()) {
                num += s2.top();
                s2.pop();
            }

            ListNode* node = new ListNode(num % 10, next);
            next = node;
            carry = num / 10;
        }

        if (carry) {
            ListNode* node = new ListNode(1, next);
            return node;
        } else {
            return next;
        }
    }
};