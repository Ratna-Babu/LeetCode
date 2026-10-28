class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            s_sum = 0
            for digit in str(n):
                s_sum += int(digit)**2
            n = s_sum
            
        return n==1
