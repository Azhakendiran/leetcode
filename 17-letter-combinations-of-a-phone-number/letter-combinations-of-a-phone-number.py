class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result: List[str] = []
        path: List[str] = []

        def backtrack(idx: int) -> None:
            if idx == len(digits):
                result.append("".join(path))
                return

            for char in keypad[digits[idx]]:
                path.append(char)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)
        return result