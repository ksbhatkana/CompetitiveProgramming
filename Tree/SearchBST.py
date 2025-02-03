class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, key: int) -> bool:
        if not root:
            return False  # ❌ Not found
        
        if root.val == key:
            return True  # ✅ Found
        
        if key < root.val:
            return self.searchBST(root.left, key)  # 🔍 Search left
        else:
            return self.searchBST(root.right, key)  # 🔍 Search right
