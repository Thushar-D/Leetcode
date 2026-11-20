class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num > 0:
                digit = num % 10
                digit_sum += digit
                num //= 10

        return abs(element_sum - digit_sum)