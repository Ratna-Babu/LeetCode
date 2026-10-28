class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = 0
        neg = False

        if x<0:
            neg = True
            x *= -1

        while x>0:
            reverse_num = (reverse_num * 10) + (x%10)
            x = x//10
        
        if reverse_num > 2**31 -1:
            return 0

        return reverse_num * -1 if neg else reverse_num