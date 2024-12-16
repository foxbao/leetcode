

#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        ListNode* dummyHead=new ListNode(0);
        dummyHead->next=head;
        ListNode* cur=dummyHead;
        while(cur->next!=nullptr && cur->next->next!=nullptr){
            ListNode* tmp=cur->next;
            ListNode* tmp1=cur->next->next->next;

            cur->next=cur->next->next;
            cur->next->next=tmp;
            cur->next->next->next=tmp1;
            cur=cur->next->next;
        }
        ListNode* result=dummyHead->next;
        delete dummyHead;
        return result;
    }
};

// 打印链表
void printList(ListNode *head)
{
    while (head)
    {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// 释放链表内存
void freeList(ListNode *head)
{
    while (head)
    {
        ListNode *temp = head;
        head = head->next;
        delete temp;
    }
}

ListNode *createTestList()
{
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    return head;
}

int main()
{
    ListNode *head = createTestList();
    Solution solution;
    ListNode *new_head = solution.swapPairs(head);
    printList(new_head);
}