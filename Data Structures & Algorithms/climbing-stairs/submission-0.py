class Solution:
    def climbStairs(self, n: int) -> int:
        # f[i] = f[i-1] + f[i-2]
        prev = 0
        curr = 1
        for i in range(n):
            next = prev + curr
            prev = curr
            curr = next
        return curr
