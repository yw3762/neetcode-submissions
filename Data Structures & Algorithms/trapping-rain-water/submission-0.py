class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0] * n
        # for each i in water, it stores max( min(highest left, highest right) - height[i], 0) amount of water, the total water trapped is just sum of water.

        left_max = [0] * (n+1)
        right_max = [0] * (n+1)

        for i in range(n):
            left_max[i+1] = max(left_max[i], height[i])
            right_max[n-i-1] = max(right_max[n-i], height[n-i-1])

        res = 0
        for i in range(n):
            res += min(left_max[i+1], right_max[i]) - height[i]
        return res