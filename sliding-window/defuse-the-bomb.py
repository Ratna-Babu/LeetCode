class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        if k == 0:
            return [0]*n

        decrypted_code = [0]*n
        code = code*2

        if k > 0:
            window_sum = sum(code[1:k+1])
            decrypted_code[0] = window_sum
            for i in range(1, n):
                window_sum = window_sum - code[i] + code[i + k]
                decrypted_code[i] = window_sum
        else:
            k = -k
            window_sum = sum(code[n - k : n])
            decrypted_code[0] = window_sum
            for i in range(1, n):
                window_sum = window_sum - code[i - 1 + n - k] + code[i - 1]
                decrypted_code[i] = window_sum

        return decrypted_code

        