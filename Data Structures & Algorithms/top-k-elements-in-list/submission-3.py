class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        for num in nums:
            res[num]+=1
        sorted_nums=sorted(res,key=res.get,reverse="true")     
        return sorted_nums[:k]