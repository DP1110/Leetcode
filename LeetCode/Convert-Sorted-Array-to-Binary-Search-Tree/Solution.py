1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def sortedArrayToBST(self, nums):
10        def helper(left, right):
11            if left > right:
12                return None
13            
14            mid = (left + right) // 2
15            root = TreeNode(nums[mid])
16            root.left = helper(left, mid - 1)
17            root.right = helper(mid + 1, right)
18            return root
19        
20        return helper(0, len(nums) - 1)