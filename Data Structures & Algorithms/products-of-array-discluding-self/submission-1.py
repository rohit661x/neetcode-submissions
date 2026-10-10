class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []

        left_product = 1
        for num in nums:
            answer.append(left_product)
            left_product *= num

        right_product = 1
        for index in range(len(nums) - 1, -1, -1):
            answer[index] *= right_product
            right_product *= nums[index]

        return answer