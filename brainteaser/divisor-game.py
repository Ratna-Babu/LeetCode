class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 2:
            return False
        dp = [False] * (n + 1)
        dp[0], dp[1] = False, False
        for i in range(2, n + 1):
            for x in range(1, i // 2 + 1):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]