class Solution(object):
    def sumOfLeftLeaves(self, root):
        
        if root == None:
            return 0
        if root.left and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
