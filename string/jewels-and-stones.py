class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = {}
        for ch in stones:
            counter[ch] = counter.get(ch,0) + 1

        count = 0

        for i in jewels:
            if i in counter:
                count += counter[i]

        return count