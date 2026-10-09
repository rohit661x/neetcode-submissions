class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for letter in s:
            if letter not in freq:
                freq[letter] = 1
            else:
                freq[letter] += 1

        for letter in t:
            if letter not in freq:
                freq[letter] = -1
            else:
                freq[letter] -= 1

        for letter in freq:
            if freq[letter] != 0:
                return False

        return True