# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # best case
        if head is None or head.next is None:
            return head
        
        # swap the nodes in reverse
        # each recursive call swaps two pairs in the list
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
        