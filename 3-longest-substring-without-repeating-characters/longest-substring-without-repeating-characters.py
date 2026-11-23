class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If char was seen inside the current window [left, right], move left past it
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len