class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def solve(arr):
            n=len(arr)
            memo={}
            def dfs(i):
                if i >= n:
                    return 0
                if i in memo:
                    return memo[i]
                rob=arr[i]+dfs(i+2)
                skip=dfs(i+1)
                memo[i]=max(rob,skip)
                return memo[i]
            return dfs(0)
        return max(solve(nums[1:]),solve(nums[:-1]))