class Solution(object):
    def sortedSquares(self, nums):
      n = len(nums)
      res = [0] * n
      i, j, k = 0, n - 1, n - 1
      while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            res[k] = nums[i] ** 2
            i += 1
        else:
            res[k] = nums[j] ** 2
            j -= 1
        k -= 1
      return res