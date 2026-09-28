class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort to easily skip duplicates and use two pointers
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # Skip duplicate values for the second and third numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1  # Need a larger sum, move left pointer right
                else:
                    k -= 1  # Need a smaller sum, move right pointer left

        return result