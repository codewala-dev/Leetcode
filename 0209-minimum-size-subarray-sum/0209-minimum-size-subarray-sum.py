class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        cur_sum = 0
        res = float('inf')

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return res if res != float('inf') else 0   

        