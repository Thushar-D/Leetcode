class Solution(object):
    def sortedSquares(self, nums):
        result = []

        for num in nums:
            square = num * num
            result.append(square)

        result.sort()

        return result