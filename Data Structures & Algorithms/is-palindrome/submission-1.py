class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = []

        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())

        left = (len(cleaned) - 1) // 2
        right = len(cleaned) // 2

        while left >= 0 and right < len(cleaned):
            if cleaned[left] != cleaned[right]:
                return False

            left -= 1
            right += 1

        return True