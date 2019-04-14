class Solution(object):
    def binaryTreePaths(self, root):
      
        result = []
        s = ''
        if root == None:
            return result
        self.search(root,result,s)
        return result
    
    def search(self,root,result,s):
        if len(s) != 0:
            s= s+'->'+str(root.val)
        else:
            s= s + str(root.val)
        if root.left == None and root.right == None:
            result.append(s)
            return
        if root.left!= None:
            self.search(root.left, result,s)
        if root.right != None:
            self.search(root.right,result,s)
