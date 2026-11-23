class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)      # -2147483648
        INT_MAX = (2**31) - 1    #  2147483647

        n = len(s)
        i = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # 2. Check optional sign
        sign = 1
        if i < n and s[i] in ("+", "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. Convert consecutive digits and handle 32-bit clamping
        result = 0
        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")

            # Clamp if adding this digit exceeds 32-bit signed integer bounds
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result