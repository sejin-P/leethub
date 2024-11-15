# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        _, numPairs = self.calculateLeafDistances(root, distance)
        return numPairs
     
    # calculate each distances and return (distances from root, number of pairs)
    def calculateLeafDistances(self, root, distance):
        if not root:
            return ([0]*11, 0)
        if not root.left and not root.right:
            return ([1]+[0]*10, 0)
        
        left = self.calculateLeafDistances(root.left, distance)
        right = self.calculateLeafDistances(root.right, distance)
        
        distanceCnts = [0]*11
        
        for i in range(10):
            distanceCnts[i+1] = left[0][i]+right[0][i]
        
        numPairs = left[1] + right[1]
        
        prefix = 0
        i = 0
        
        for d in range(distance-2, -1, -1):
            prefix += left[0][i]
            numPairs += prefix * right[0][d]
            i += 1
        
        return (distanceCnts, numPairs)
        