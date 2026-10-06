class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []

        if n < 4:
            return res

        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # --- Pruning for Loop 1 ---
            # Smallest 4-sum starting with nums[i] exceeds target -> impossible to form target later
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Largest 4-sum starting with nums[i] is below target -> nums[i] is too small
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # --- Pruning for Loop 2 ---
                # Smallest 3-sum starting with nums[j] exceeds target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Largest 3-sum starting with nums[j] is below target
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                # Two-pointer sweep for remaining 2 elements
                k = j + 1
                l = n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1

                        k += 1
                        l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1

        return res
        