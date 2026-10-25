class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        available = {}

        for char in magazine:
            available[char] = available.get(char, 0) + 1

        for char in ransomNote:
            if char not in available or available[char] == 0:
                return False

            available[char] -= 1

        return True