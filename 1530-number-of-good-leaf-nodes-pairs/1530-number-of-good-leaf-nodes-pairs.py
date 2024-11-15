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
            return ([], 0)
        
        left = self.calculateLeafDistances(root.left, distance)
        right = self.calculateLeafDistances(root.right, distance)
        
        if not left[0] and not right[0]:
            return ([0], 0)
        
        distances = []
        
        for d in left[0]:
            distances.append(d+1)
        for d in right[0]:
            distances.append(d+1)
        
        numPairs = left[1] + right[1]
        for ld in left[0]:
            for rd in right[0]:
                if ld + rd + 2 <= distance:
                    numPairs += 1
        
        return (distances, numPairs)
        