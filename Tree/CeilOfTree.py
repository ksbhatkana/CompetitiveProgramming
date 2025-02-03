class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findCeil(self, root: TreeNode, key: int) -> int:
        ceil = -1  # Default if no ceil exists

        while root:
            if root.val == key:
                return root.val  # ✅ Exact match found

            if key < root.val:
                ceil = root.val  # ✅ Potential ceil
                root = root.left  # Move left
            else:
                root = root.right  # Move right

        return ceil
