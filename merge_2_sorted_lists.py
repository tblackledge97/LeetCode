# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # placeholder to build the list
        dummy = ListNode(0)
        # current pointer to track the last
        # node in the merge list
        # starts as a dummy as moves forward
        # as we add to the list
        current = dummy

        # while both list1 and list2 aren't empty
        while list1 and list2:
            # if list 1 value is larger than list 2 value
            # make it head of the new list
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            # otherwise make list 2 value new head
            else:
                current.next = list2
                list2 =list2.next
            # move the current pointer
            current = current.next
        
        # if list 1 still has elements
        # add remaining elements to the merge list
        if list1:
            current.next = list1
        # if list 2 still has elements
        # add remaining elements to the merge list
        elif list2:
            current.next = list2
        
        # return head of the merge list
        return dummy.next