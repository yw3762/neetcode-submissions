class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        res = []

        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]
        
        prefix = 1
        for i in range(n - 1, -1 , -1):
            res[i] *= prefix
            prefix *= nums[i]

        return res