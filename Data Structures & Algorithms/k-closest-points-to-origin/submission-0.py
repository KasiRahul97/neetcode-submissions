class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=defaultdict(int)
        count=0
        l=[]
        for pt in points:
            d[tuple(pt)]=pt[0]*pt[0]+pt[1]*pt[1]
        ds=dict(sorted(d.items(),key=lambda x:x[1]))
        for dist in ds:
            if count==k:
                break
            l.append(list(dist))
            count+=1
        return l