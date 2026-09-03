class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def check(ds:List[int],freq:defaultdict[int]):
            if len(ds)==len(nums):
                ans.append(ds[:])
                return
            for i in range(len(nums)):
                if freq[i]==0:
                    ds.append(nums[i])
                    freq[i]+=1
                    check(ds,freq)
                    ds.pop()
                    freq[i]-=1
        check([],defaultdict(int))
        return ans