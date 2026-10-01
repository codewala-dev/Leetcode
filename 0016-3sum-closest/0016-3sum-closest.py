class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == target:
                    return total  # Exact match found, can return immediately
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                    
                if total < target:
                    j += 1
                else:
                    k -= 1

        return closest_sum


        