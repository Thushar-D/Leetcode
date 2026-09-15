class Solution(object):
    def maxSubArray(self, nums):
        max_i = float("-inf")
        total = 0

        for i in range(len(nums)):
            total = total + nums[i]

            max_i = max(max_i, total)

            if total < 0:
                total = 0

        return max_i