class Solution(object):
    def rearrangeArray(self, nums):
        result = [0] * len(nums)

        posIndex = 0
        negIndex = 1

        for num in nums:
            if num > 0:
                result[posIndex] = num
                posIndex += 2
            else:
                result[negIndex] = num
                negIndex += 2

        return result