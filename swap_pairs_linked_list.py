# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if the list has less than 2 heads, return head (best case)
        if head is None or head.next is None:
            return head
            
        # save the remaining list
        remaining_list_head = head.next.next

        # swap the heads 
        new_head = head.next
        new_head.next = head
        head.next = self.swapPairs(remaining_list_head)
        return new_head
