class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow_set = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        s = list(s)
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] not in vow_set:
                left_pointer += 1
            if s[right_pointer] not in vow_set:
                right_pointer -= 1
            if s[right_pointer] in vow_set and s[left_pointer] in vow_set:
                s[right_pointer], s[left_pointer] = s[left_pointer], s[right_pointer]
                left_pointer += 1
                right_pointer -= 1

        return ''.join(s)
