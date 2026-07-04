# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = set()
        queue = deque()
        res = []

        if not root:
            return []
        
        queue.append((1, root))

        while queue:
            height, node = queue.popleft()
            if height not in seen:
                seen.add(height)
                res.append(node.val)
            
            if node.right:
                queue.append((1 + height, node.right))
            if node.left:
                queue.append((1 + height, node.left))
            
        return res
        