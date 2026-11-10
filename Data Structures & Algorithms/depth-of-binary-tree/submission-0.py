# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_node = root.left
        right_node = root.right
        if left_node is None and right_node is None:
            return 1
        elif left_node is not None and right_node is None:
            return 1 + self.maxDepth(left_node)
        elif right_node is not None and left_node is None:
            return 1 + self.maxDepth(right_node)
        else:
            return 1 + max(self.maxDepth(left_node), self.maxDepth(right_node))