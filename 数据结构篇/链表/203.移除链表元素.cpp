

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
ListNode* removeElements(ListNode* head,int val)
{
    ListNode* dummyHead= new ListNode(0);
    dummyHead->next=head;
    ListNode* cur=dummyHead;
    while(cur->next!=NULL)
    {
        if(cur->next->val==val)
        {
            ListNode* temp=cur->next;
            cur->next=cur->next->next;
            delete temp;
        }
        else
        {
            cur=cur->next;
        }
    }
    head=dummyHead->next;
    delete dummyHead;
    return head;
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
    int val=4;
    ListNode* new_head=solution.removeElements(head,val);
    printList(new_head);
}