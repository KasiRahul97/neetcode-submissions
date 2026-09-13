#memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        n=len(nums)
        def solve(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            rob=nums[i]+solve(i+2)
            skip=solve(i+1)
            memo[i]=max(rob,skip)
            return memo[i]
        return solve(0)