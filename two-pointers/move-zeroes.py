class Solution(object):
    def moveZeroes(self, nums):
        
        left_pointer = 0
        l = len(nums)

        for i in range(l):
            if nums[i] != 0:
                nums[left_pointer] = nums[i]
                left_pointer += 1
        
        for i in range(left_pointer,l):
            nums[i] = 0

        return nums

        