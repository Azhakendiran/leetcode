class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes; numbers ending with 0
        # (except 0 itself) cannot be palindromes without leading zeros.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: middle digit is in reversed_half, so reversed_half // 10
        return x == reversed_half or x == reversed_half // 10