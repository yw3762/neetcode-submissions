class Solution:
    def rob_linear(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))