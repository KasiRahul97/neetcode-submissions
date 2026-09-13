#Memoization    
class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def solve(i):
            if i>n:
                return 0
            if i==n:
                return 1
            if i in memo:
                return memo[i]
            memo[i]=solve(i+1)+solve(i+2)
            return memo[i]
        return solve(0)