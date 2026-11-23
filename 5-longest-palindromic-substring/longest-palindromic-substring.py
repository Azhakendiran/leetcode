class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        best_start = 0
        best_len = 1

        def expand_around_center(left: int, right: int) -> None:
            nonlocal best_start, best_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > best_len:
                    best_start = left
                    best_len = curr_len
                left -= 1
                right += 1

        for i in range(len(s)):
           
            expand_around_center(i, i)
            # Even-length palindrome centered between i and i + 1 (e.g., "abba")
            expand_around_center(i, i + 1)

        return s[best_start : best_start + best_len]