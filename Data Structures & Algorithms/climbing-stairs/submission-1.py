class Solution:
    def climbStairs(self, n: int) -> int:
        # f[i] = f[i-1] + f[i-2]
        prev = 1
        curr = 1
        for i in range(n-1):
            next = prev + curr
            prev = curr
            curr = next
        return curr
