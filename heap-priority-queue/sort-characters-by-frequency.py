class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        freq_list = []
        for ch in freq:
            freq_list.append((ch, freq[ch]))

        def sort_desc(frequency_list):
            return -frequency_list[1]

        freq_list.sort(key=sort_desc)

        result = ''
        for ch, f in freq_list:
            result += ch * f
        
        return result