class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        nums = sorted(nums)

        left_pointer = 0
        right_pointer = len(nums)-1

        while left_pointer<right_pointer:
            total = nums[left_pointer] + nums[right_pointer]
            if total == k:
                count+=1
                left_pointer += 1
                right_pointer -= 1
                continue
            if total < k:
                left_pointer += 1
            else:
                right_pointer -= 1
        return count