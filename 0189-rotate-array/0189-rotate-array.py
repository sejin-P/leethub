class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        if k == 0:
            return
        
        rotated = 0
        rotated_num = nums[0]
        i, start = 0, 0
        
        while rotated < n:
            rotated_num, nums[(i+k)%n] = nums[(i+k)%n], rotated_num
            rotated += 1
            i = (i+k)%n
            if i == start:
                i = (i+1)%n
                start += 1
                rotated_num = nums[i]
        