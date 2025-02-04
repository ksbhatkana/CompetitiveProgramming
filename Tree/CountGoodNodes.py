from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Check if current node is a "good node"
            good = 1 if node.val >= max_so_far else 0

            # Update max_so_far for the next level
            new_max = max(max_so_far, node.val)

            # Recursively count good nodes in left and right subtrees
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)

            return good

        return dfs(root, root.val)  # Start with root's value as max_so_far
