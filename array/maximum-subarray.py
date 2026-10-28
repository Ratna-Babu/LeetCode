class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum_nums = 0 
        max_subarray = float('-inf')

        for i in range(len(nums)):
            sum_nums = max(sum_nums + nums[i], nums[i])
            max_subarray = max(sum_nums, max_subarray)

        return max_subarray
        