class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        v_count = 0

        for i in range(k):
            if s[i] in vowels:
                v_count += 1
        max_count = v_count

        for i in range(k,len(s)):
            if s[i-k] in vowels:
                v_count -= 1
            if s[i] in vowels:
                v_count += 1

            max_count = max(v_count, max_count)

        return max_count