from collections import Counter
class Solution(object):
    def customSortString(self, order, s):
        count = Counter(s)
        result = ''
        for ch in order:
            if ch in count:
                result += ch*count[ch]
                count[ch] = 0
        for ch in count:
            result += ch*count[ch]
        return result
 
        