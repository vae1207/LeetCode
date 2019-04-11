class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
 
        r1 = max(p.val,q.val)
        r2 = min(p.val,q.val)
        while root:
            if root.val>= r2 and root.val<=r1:
                return root
            if root.val>r1:
                root = root.left
            else:
                root = root.right
        return root
