from collections import deque, defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bottomView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        column_map = {}  # Stores {column: (row, value)}
        queue = deque([(root, 0, 0)])  # (node, column, row)

        while queue:
            node, col, row = queue.popleft()
            column_map[col] = (row, node.val)  # Store the last encountered node in each column

            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        # Extract values sorted by column index
        return [column_map[col][1] for col in sorted(column_map.keys())]
