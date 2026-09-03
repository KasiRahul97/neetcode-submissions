class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=defaultdict(int)
        for num in nums:
            f[num]+=1
        bucket=[[] for _ in range(len(nums)+1)]
        for num,count in f.items():
            bucket[count].append(num)
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            for elt in bucket[i]:
                ans.append(elt)
            if len(ans)==k:
                return ans
        return []