class Solution(object):
    def longestConsecutive(self, nums):
        my_set = set(nums)

        longest = 0

        for num in my_set:
            if num - 1 not in my_set:
                count = 1
                x = num

                while x + 1 in my_set:
                    count += 1
                    x += 1

                longest = max(longest, count)

        return longest