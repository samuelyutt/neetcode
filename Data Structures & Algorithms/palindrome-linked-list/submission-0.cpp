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
    bool isPalindrome(ListNode* head) {
        string s;
        ListNode* node = head;
        while (node != nullptr) {
            s += node->val;
            node = node->next;
        }
        return isPalindrome(s, 0);
    }

    bool isPalindrome(string& s, int i) {
        int j = s.size() - i - 1;
        if (j - i <= 1) {
            return s[i] == s[j];
        } else {
            return (s[i] == s[j]) && isPalindrome(s, i + 1);
        }
    }
};