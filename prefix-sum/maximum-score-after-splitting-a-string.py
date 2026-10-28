class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_zero = 0
        right_one = 0
        for i in range(len(s)):
            if s[i]=='1':
                right_one += 1
        score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zero += 1
            else:
                right_one -= 1
            total_sum = left_zero+right_one
            if total_sum > score:
                score = total_sum
        return score
