from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        maxHeap = []
        heapify(maxHeap)
        for i in range(min(len(nums1), k)):
            for j in range(min(len(nums2), k)):
                pair = [nums1[i], nums2[j]]
                if len(maxHeap) < k:
                    heappush(maxHeap, [-1*(nums1[i] + nums2[j]), pair])
                else:
                    if nums1[i] + nums2[j] > -maxHeap[0][0]:
                        break
                    heappush(maxHeap, [-1*(nums1[i] + nums2[j]), pair])
                    heappop(maxHeap)
                    
        pairs = [] 
        for val in maxHeap:
            pairs.append(val[1])
        return pairs
        