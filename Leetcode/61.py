# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # list is [], return None
        if head == None:
            return None
        
        # calculate length of cycle and get tail of list
        count = 1
        p = head
        while(p.next):
            count += 1
            p = p.next
        
        # change it into cycle list
        p.next = head
        
        # calculate the movement of point
        count = count - k % count
        
        while(count):
            p = head
            head = head.next
            count -= 1
        p.next = None
        return head