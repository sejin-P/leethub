class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        ret = []
        unserscore_ret = []
        prev_num = -101
        for num in nums:
            if num != prev_num:
                nums[cnt] = num
                cnt += 1
                ret.append(num)
                prev_num = num
        
        return cnt
        