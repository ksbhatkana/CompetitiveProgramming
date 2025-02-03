from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            if level == len(result):  # ✅ First node at this level
                result.append(node.val)
            
            dfs(node.left, level + 1)  # ✅ Prioritize left child first
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result

    def rightView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            if level == len(result):  # ✅ First node at this level
                result.append(node.val)
            
            dfs(node.right, level + 1)  # ✅ Prioritize right child first
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result
