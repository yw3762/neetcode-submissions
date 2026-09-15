class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_prod = [1] * (n+1)
        backward_prod = [1] * (n+1)

        for i in range(n):
            forward_prod[i+1] = forward_prod[i] * nums[i]
            backward_prod[n - i - 1] = backward_prod[n - i] * nums[n - i - 1]
        
        res = [0] * n
        for i in range(n):
            res[i] = forward_prod[i] * backward_prod[i+1]

        return res