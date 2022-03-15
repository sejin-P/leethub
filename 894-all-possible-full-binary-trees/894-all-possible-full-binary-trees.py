# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return None
        if n == 1:
            return [TreeNode()]
        
        results = [[TreeNode()]]
        for i in range(3, n+1, 2):
            graphs = []
            for j in range(i-2, 0, -2):
                for left_graph in results[(j-1)//2]:
                    for right_graph in results[(i-j-1)//2]:
                        base_graph = TreeNode()
                        base_graph.left = left_graph
                        base_graph.right = right_graph
                        graphs.append(base_graph)
            results.append(graphs)
       
                   
        return results[(n-1)//2]
        