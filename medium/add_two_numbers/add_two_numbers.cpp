#include <iostream>

struct ListNode {
   int val;
   ListNode *next;
   ListNode() : val(0), next(nullptr) {}
   ListNode(int x) : val(x), next(nullptr) {}
   ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *add_two_numbers(ListNode *l1, ListNode *l2) {
   ListNode *ret = new ListNode();
   ListNode *temp = ret;
   int carried = 0;
   while (l1 || l2 || carried) {
      int sum = 0;
      if (l1) {
         sum += l1->val;
         l1 = l1->next;
      }
      if (l2) {
         sum += l2->val;
         l2 = l2->next;
      }
      if (sum + carried > 9) {
         temp->val = (sum + carried) % 10;
         carried = 1;
      } else {
         temp->val = sum + carried;
         carried = 0;
      }
      if (l1 || l2 || carried) {    
         ListNode *new_node = new ListNode();
         temp->next = new_node;
         temp = temp->next;
      }
   }
   return ret;
}

int main() {
   int size;
   ListNode l1, l2, *l1_ptr, *l2_ptr;
   l1_ptr = &l1;
   l2_ptr = &l2;
   scanf("%d", &size);
   scanf("%d", &l1_ptr->val);
   for (int i = 1; i < size; i++) {
      l1_ptr->next = new ListNode();
      l1_ptr = l1_ptr->next;
      scanf("%d", &l1_ptr->val);
   }
   scanf("%d", &size);
   scanf("%d", &l2_ptr->val);
   for (int i = 1; i < size; i++) {   
      l2_ptr->next = new ListNode();     
      l2_ptr = l2_ptr->next;
      scanf("%d", &l2_ptr->val);
   }
   ListNode *ret = add_two_numbers(&l1, &l2);
   while (ret) {
      std::cout << "->";
      std::cout << ret->val;
      ret = ret->next;
   }
   std::cout << "\n";
}

