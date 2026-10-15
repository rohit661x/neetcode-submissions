class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if stack[-1] != matches[char]:
                    return False
                
                stack.pop()
        return not stack