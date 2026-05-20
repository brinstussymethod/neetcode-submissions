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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // we need to multiply ones places, tens places, hundreds place, etc.. 
        // we need to consider the carrying over a number 9 + 6 = 15 where 1 was carried over. 
        // we need to maniplulate a linked list or just make a new one and return it's head. 
        // we will compute an integer and make the new linked list starting from the 1's place up -> 

        ListNode dummy(0); 
        ListNode* tail = &dummy; 
        int carry = 0; 
    
        
        while(l1 || l2 || carry) {
            int a = l1 ? l1->val  : 0; 
            int b = l2 ? l2->val : 0; 

            int sum = a + b + carry; 
            int digit = sum % 10;
            carry = sum / 10; 

            tail->next = new ListNode(digit); 
            tail = tail->next; 

            if (l1) l1 = l1->next; 
            if (l2) l2 = l2->next; 
            
        }
        
       return dummy.next; 
    }
};
