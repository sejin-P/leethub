from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        
        values = cnt.values()
        min_val = min(values)
        max_val = max(values)
        
        c = [0]*(max_val-min_val+1)

        val_dict = defaultdict(list)
        for key in cnt.keys():
            c[cnt[key]-min_val] += 1
            val_dict[cnt[key]-min_val].append(key)
       
        res = []
        for i in range(len(c)-1,-1,-1):
            k -= c[i]
            res += val_dict[i]
            if k == 0:
                return res
        