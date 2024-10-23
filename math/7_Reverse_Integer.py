class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        
        reverse_num = str(abs(x))[::-1]
        
        result = sign * int(reverse_num)

        if result < -2**31 or 2**31 < result:
            return 0
            
        return result