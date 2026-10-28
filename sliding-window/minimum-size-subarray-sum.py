class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        right, left = 0, 0
        window_sum = 0
        min_len = float('inf')
        while right < len(nums):
            window_sum += nums[right]
            while window_sum >= target:
                min_len = min(min_len,right-left+1)
                window_sum -= nums[left]
                left += 1
            right += 1
        
        if min_len == float('inf'): return 0
        return min_len
            



        
        

            