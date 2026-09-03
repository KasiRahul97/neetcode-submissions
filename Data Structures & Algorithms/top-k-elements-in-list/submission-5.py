class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=0
        res=[]
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        x=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        for ch in x:
            if c!=k:
                res.append(ch)
                c+=1
        return res