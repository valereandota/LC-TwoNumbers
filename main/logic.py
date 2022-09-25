# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ll_to_int(self, ll):
        string_value= ""
        values = []
        values.append(str(ll.val))
        while ll.next:
            current_value = ll.next.val
            values.append(str(current_value))
            ll = ll.next
        for i in reversed(values):
            string_value += i
        return int(string_value)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_of_vals = self.ll_to_int(l1) + self.ll_to_int(l2)
        return_list = []
        for i in reversed(str(sum_of_vals)):
            return_list.append(int(i)) 
        ret_ll = None
        for i in str(sum_of_vals): 
            ret_ll = ListNode(int(i), next = ret_ll)
        return ret_ll
            