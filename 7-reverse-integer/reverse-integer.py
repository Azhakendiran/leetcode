class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)      # -2147483648
        INT_MAX = (2**31) - 1    #  2147483647

        sign = -1 if x < 0 else 1
        num = abs(x)
        rev = 0

        while num != 0:
            digit = num % 10
            num //= 10

            # Check overflow before `rev = rev * 10 + digit`
            # Compare against positive bound first, then adjust for sign
            limit = INT_MAX if sign == 1 else abs(INT_MIN)
            if rev > limit // 10 or (rev == limit // 10 and digit > limit % 10):
                return 0

            rev = rev * 10 + digit

        return sign * rev