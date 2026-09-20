class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each i < n - 2, find two sum in nums[i+1:] 
        # that sums to -nums[i]
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        n = len(nums)
        res = []
        for i in range(n):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, n):
                count[nums[j]] -= 1
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                target = - nums[i] - nums[j]
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, n):
                count[nums[j]] += 1

        return res