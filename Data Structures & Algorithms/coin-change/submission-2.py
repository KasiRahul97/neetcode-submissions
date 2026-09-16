class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def solve(amt):
            if amt==0:
                return 0
            if amt<0:
                return 1e9
            if amt in memo:
                return memo[amt]
            res=1e9
            for coin in coins:
                if amt-coin>=0:
                    res=min(res,1+solve(amt-coin))
                    memo[amt]=res
            return res
        mincoins=solve(amount)
        return -1 if mincoins>=1e9 else mincoins
                        
                