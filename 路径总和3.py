class Solution(object):
    def __init__(self):
        self.pathNum = 0
    def pathSum(self, root, sum):
      
        def dfs(root,s):
            
            if not root:
                return 
            if s == root.val:
                self.pathNum += 1
            dfs(root.left,s-root.val)
            dfs(root.right,s - root.val)
        
        if not root:
            return 0
        dfs(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        return self.pathNum
