

#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x):val(x),next(NULL){}
};

class Solution
{
public:
ListNode* reverseList(ListNode* head)
{
    ListNode* temp;
    ListNode* cur=head;
    ListNode* pre=NULL;
    while(cur)
    {
        temp=cur->next;
        cur->next=pre;
        pre=cur;
        cur=temp;
    }
    return pre;
}
};

// 打印链表
void printList(ListNode* head) {
    while (head) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// 释放链表内存
void freeList(ListNode* head) {
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

ListNode* createTestList(){
    ListNode* head= new ListNode(1);
    head->next= new ListNode(2);
    head->next->next= new ListNode(3);
    head->next->next->next= new ListNode(4);
    head->next->next->next->next= new ListNode(5);
    return head;


}

int main()
{
    ListNode* head=createTestList();
    Solution solution;
    ListNode* new_head=solution.reverseList(head);
    printList(new_head);
}