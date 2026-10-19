class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n=len(nums)
        res,csum,left=float('inf'),0,0

        if n==0:
            return 0

        for right in range(n):
            csum+=nums[right]

            while csum >=target:
              res=min(res,right-left+1)
              csum-=nums[left]
              left+=1
        return res  if res != float('inf') else 0
