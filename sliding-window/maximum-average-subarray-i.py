class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg = sum(nums[:k])
        max_avg = avg

        for i in range(k,len(nums)):
            avg += nums[i] - nums[i-k]
            if avg>max_avg:
                max_avg = avg

        return max_avg/float(k)
