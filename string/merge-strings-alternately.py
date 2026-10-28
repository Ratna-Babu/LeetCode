class Solution(object):
    def mergeAlternately(self, word1, word2):
        l = len(word1) + len(word2)

        result = ''
        p1, p2 = 0, 0
        while len(result) != l:
            if p1<len(word1):
                result+=(word1[p1])
                p1+=1
            if p2<len(word2):
                result+=(word2[p2])
                p2+=1
        
        return result