# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Go through every node, and swap its left and right nodes
        if root is None:
            return None
        left_node = root.left
        right_node = root.right
        if left_node is None and right_node is None:
            return root
        elif left_node is None and right_node is not None:
            root.right = None
            root.left = self.invertTree(right_node)
            return root
        elif left_node is not None and right_node is None:
            root.left = None
            root.right = self.invertTree(left_node)
            return root
        else: # Both nodes exist
            root.left = self.invertTree(right_node)
            root.right = self.invertTree(left_node)
            return root
