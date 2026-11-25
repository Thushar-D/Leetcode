class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        i = 0
        n = len(s)
        longest = 0

        while i < n:
            zeros = 0
            ones = 0

            while i < n and s[i] == '0':
                zeros += 1
                i += 1

            while i < n and s[i] == '1':
                ones += 1
                i += 1

            longest = max(longest, 2 * min(zeros, ones))

        return longest
        