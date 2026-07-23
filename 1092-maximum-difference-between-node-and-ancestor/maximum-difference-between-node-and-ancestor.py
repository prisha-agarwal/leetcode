# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0 
        queue = deque([(root, root.val, root.val)])

        while queue: 
            node, cur_min, cur_max = queue.popleft() 
            result = max(result, abs(node.val-cur_min), abs(node.val-cur_max))
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            if node.left: 
                queue.append((node.left, cur_min, cur_max))
            if node.right: 
                queue.append((node.right, cur_min, cur_max))
        
        return result
        