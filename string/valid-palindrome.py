class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_pointer, right_pointer = 0, len(s)-1
        while left_pointer<right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue
            if s[left_pointer].lower() == s[right_pointer].lower():
                left_pointer += 1
                right_pointer -= 1
            else:
                return False
        return True
        