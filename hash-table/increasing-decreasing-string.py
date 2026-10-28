from collections import Counter
class Solution(object):
    def sortString(self, s):
        count = Counter(s)

        result = []
        while len(result) != len(s):
            for ch in sorted(count.keys()):
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1

            for ch in sorted(count.keys(), reverse=True):
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1
        
        return ''.join(result)
        