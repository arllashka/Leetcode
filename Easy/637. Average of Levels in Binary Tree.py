from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ls = []
        while q:
            n = len(q)
            levelsum = 0

            
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                levelsum+=node.val
            ls.append(levelsum/n)
            
        return ls