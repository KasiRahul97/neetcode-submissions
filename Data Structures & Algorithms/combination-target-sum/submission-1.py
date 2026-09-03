class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def answer(ind:int,ds:List[int],target:int):
            if ind==len(nums):
                if target==0:
                    #ans.append(ds) if ds.append(2); first ans=[[2]]. but later if ds.appned(3), ans=[[2,3] so use copy
                    ans.append(ds[:])
                return
            if nums[ind]<=target:
                ds.append(nums[ind])
                answer(ind,ds,target-nums[ind])
                ds.pop()
            answer(ind+1,ds,target)
        answer(0,[],target)
        return ans
            
