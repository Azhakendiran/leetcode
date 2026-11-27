class Solution:
    def isValid(self, s: str) -> bool:
        # Odd-length strings cannot have every bracket paired
        if len(s) % 2 == 1:
            return False

        matching_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack: list[str] = []

        for char in s:
            if char in matching_open:
                if not stack or stack[-1] != matching_open[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0