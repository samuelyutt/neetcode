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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* node = head;
        ListNode* next = nullptr;

        while (node) {
            while (node && node->val == val) {
                if (node == head)
                    head = node->next;
                node = node->next;
            }

            if (node) {
                next = node->next;
                while (next && next->val == val) {
                    next = next->next;
                }

                node->next = next;
            }

            node = next;
        }

        return head;
    }
};