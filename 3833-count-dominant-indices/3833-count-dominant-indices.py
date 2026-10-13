class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        right_sum = sum(nums)
        for i in range(n - 1):
            right_sum -= nums[i]
            right_count = n - i - 1
            if nums[i] * right_count > right_sum:  
                right_count
                count += 1
        return count   