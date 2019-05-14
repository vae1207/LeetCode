class Solution(object):
    def levelOrder(self, root):
        
        if not root:
            return []
        queue =[root]
        ans = []
        while queue:
            layer = []
            next_queue = []
            while queue:
                node = queue.pop(0)
                layer.append(node.val)
                next_queue.extend(node.children)
            ans.append(layer)
            queue = next_queue
        return ans
