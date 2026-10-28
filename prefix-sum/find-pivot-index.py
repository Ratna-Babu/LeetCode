class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]

        n = len(nums)

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        for i in range(n):
            if i == 0:
                left_sum = 0
            else:
                left_sum = prefix_sum[i-1]
            right_sum = prefix_sum[n-1] - prefix_sum[i]
            if left_sum == right_sum:
                return i
        
        return -1
