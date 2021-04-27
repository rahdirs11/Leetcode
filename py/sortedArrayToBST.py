# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.findNodes(0, len(nums) - 1, nums)

    def findNodes(l, r, nums):
        if l > r:
            return None

        mid = l + (r - l) // 2
        node = TreeNode(nums[mid])
        node.left = TreeNode(l, mid - 1, nums)
        node.right = TreeNode(mid + 1, r, nums)
        return node

