class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefix_sum = [0]*n
        prefix_sum[0] = arr[0]

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]

        total_sum = 0
        for i in range(n):
            for j in range(i,n):
                length = j - i + 1
                if length % 2 == 1:
                    if i == 0:
                        total_sum += prefix_sum[j]
                    else:
                        total_sum += prefix_sum[j] - prefix_sum[i-1]
        
        return total_sum


        