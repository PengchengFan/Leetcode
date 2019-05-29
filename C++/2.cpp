/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry = 0;
        ListNode dummy_root(0);
        ListNode *root = &dummy_root;
        while (l1 || l2 || carry) {
            carry = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            root->next = new ListNode(carry % 10);
            carry = carry / 10;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
            root = root->next;
        }
        return dummy_root.next;
    }
};