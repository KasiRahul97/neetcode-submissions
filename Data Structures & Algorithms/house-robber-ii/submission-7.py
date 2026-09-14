#tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def solve(arr):
            n=len(arr)
            if n==1:
                return arr[0]
            dp=[0]*n
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],dp[i-2]+arr[i])
            return dp[n-1]
        return max(solve(nums[1:]),solve(nums[:-1]))
                