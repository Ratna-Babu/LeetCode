class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)

        for i in range(len(nums)):
            num = target-nums[i]
            if num in count:
                if num==nums[i] and count[num]>1:
                    return [i,nums.index(num,i+1)]
                elif num!=nums[i]:
                    return [i,nums.index(num)]
        