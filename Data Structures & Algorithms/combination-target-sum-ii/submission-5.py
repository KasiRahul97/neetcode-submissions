class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def answer(index:int,ds:List[int],target:int,ans:List[List[int]],candidates:List[int]):
            #if index>=len(candidates):
            if target==0:
                ans.append(ds[:])
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                answer(i+1,ds,target-candidates[i],ans,candidates)
                ds.pop()
            #answer(index+1,ds,target,ans,candidates)
        answer(0,[],target,ans,candidates)
        return ans