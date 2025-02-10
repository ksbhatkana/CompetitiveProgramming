# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = None
        if root:
            root_queue = deque([root])
            
            while root_queue:
                cur_len = len(root_queue)
                for i in range(cur_len):
                    elem = root_queue.popleft()
                    if i == 0:
                        result = elem.val
                    if elem.left:
                        root_queue.append(elem.left)
                    if elem.right:
                        root_queue.append(elem.right)
        return result
