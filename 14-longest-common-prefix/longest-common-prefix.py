class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        base = strs[0]

        for i, char in enumerate(base):
            for word in strs[1:]:
                # Stop if `word` is shorter than `i` or character differs
                if i >= len(word) or word[i] != char:
                    return base[:i]

        return base