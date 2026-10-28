class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(k):
            if k == 1:
                return 'a'
            length = 1
            while length < k:
                length *= 2
            half = length // 2
            if k <= half:
                return helper(k)
            prev = helper(k - half)
            return chr((ord(prev) - ord('a') + 1) % 26 + ord('a'))
        return helper(k)