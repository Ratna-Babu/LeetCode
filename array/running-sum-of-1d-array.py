class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [0]*len(nums)
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = nums[i]+prefix[i-1]

        return prefix