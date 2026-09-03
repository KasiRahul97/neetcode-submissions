class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks=[]
        for s in stones:
            rocks.append(-s)
        heapq.heapify(rocks)
        while len(rocks)>1:
            curr=-(heapq.heappop(rocks)-heapq.heappop(rocks))
            if curr:
                heapq.heappush(rocks,-curr)
        return -heapq.heappop(rocks) if rocks else 0
        
