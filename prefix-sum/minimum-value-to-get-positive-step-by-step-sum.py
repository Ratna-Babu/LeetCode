class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        startValue = 0
        prefix_sum = [0]*(len(nums)+1)
        while True:
            startValue += 1
            prefix_sum[0] = startValue
            flag = True
            for i in range(1,len(nums)+1):
                prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
                if prefix_sum[i]<1:
                    flag = False
                    break
            if flag:
                return startValue
            
