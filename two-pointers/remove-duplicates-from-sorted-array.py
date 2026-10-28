class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[unique]:
                unique += 1
                nums[unique] = nums[i]
        return unique + 1
        