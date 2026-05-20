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
    bool hasCycle(ListNode* head) {
        ListNode* slowpointer = head; 
        ListNode* fastpointer = head;

        while(fastpointer != nullptr && fastpointer->next != nullptr) {
            slowpointer = slowpointer->next; 
            fastpointer = fastpointer->next->next; 

            if(slowpointer == fastpointer) {
                return true; 
            }
        }   

        return false; 
    }
};
