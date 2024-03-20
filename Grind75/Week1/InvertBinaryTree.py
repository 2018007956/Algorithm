# Not Solved) TypeError: ReeNode object is not subscriptable
class Solution:
    def isPowerOf2(n):
        return (n&(n-1))==0

    def node_count(root):
        if root:
            return 1 + Solution.node_count(root.left) + Solution.node_count(root.right)
        else:
            return 0

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        for i in range(Solution.node_count(root)):
            if Solution.isPowerOf2(i+1):
                result.append(root[i:2*i+1].reverse())
        return result 
        
# 0 1 3 7 15
# 0 2-1 4-1 8-1 16-1