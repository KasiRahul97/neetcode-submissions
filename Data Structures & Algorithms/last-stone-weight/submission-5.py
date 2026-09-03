class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            n=len(stones)
            if stones[n-1]==stones[n-2]:
                stones.pop()
                stones.pop()
            elif stones[n-2]>stones[n-1]:
                stones[n-2]=stones[n-2]-stones[n-1]
                stones.pop()
            elif stones[n-1]>stones[n-2]:
                stones[n-1]=stones[n-1]-stones[n-2]
                t=stones[n-1]
                stones[n-2]=t
                stones.pop()
        if stones:
            return stones[0]
        else:
            return 0
            