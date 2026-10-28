class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        for word in strs[1:]:
        # Reduce the prefix until it matches the start of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
        