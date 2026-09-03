class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mh=[]
        for x,y in points:
            dist=-(x*x+y*y)
            heapq.heappush(mh,(dist,x,y))
        while len(mh)>k:
            heapq.heappop(mh)
        return [[x,y] for dist,x,y in mh]