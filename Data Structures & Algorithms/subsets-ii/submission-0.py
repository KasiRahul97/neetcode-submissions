class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def answer(index:int,ds:List[int],nums:List[int],ans:List):
            if index==len(nums):
                ans.append(ds[:])
                return
            ds.append(nums[index])
            answer(index+1,ds,nums,ans)
            ds.pop()
            index_next=index+1
            while index_next<len(nums) and nums[index]==nums[index_next]:
                index_next+=1
            answer(index_next,ds,nums,ans)
        answer(0,[],nums,ans)
        return ans