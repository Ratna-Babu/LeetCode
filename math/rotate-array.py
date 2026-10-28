class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums)-1
        for i in range(k):
            nums.insert(0,nums[last])
            nums.pop(last+1)