class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def answer(index:int,ds:List,nums:List[int],ans:List):
            if index==len(nums):
                ans.append(ds[:])
                return
            ds.append(nums[index])
            answer(index+1,ds,nums,ans)
            ds.pop()
            answer(index+1,ds,nums,ans)
        answer(0,[],nums,ans)
        return ans
