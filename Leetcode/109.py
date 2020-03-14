# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        arr = []
        while(head):
            arr.append(head.val)
            head.next

        return self.buildBST(arr)


    def buildBST(self, arr):
        if not arr:
            return None
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.buildBST(arr[:mid])
        root.right = self.buildBST(arr[mid + 1:])
        return root
