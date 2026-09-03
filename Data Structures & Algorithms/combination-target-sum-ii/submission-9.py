class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def answer(index:int,ds:List[int],target:int):
            if index==len(candidates):
                if target==0:
                    #ans.append(ds) if ds.append(2); first ans=[[2]]. but later if ds.appned(3), ans=[[2,3] so use copy
                    ans.append(ds[:])
                return
            if candidates[index]<=target:
                ds.append(candidates[index])
                answer(index+1,ds,target-candidates[index])
                ds.pop()
            index_next=index+1
            while index_next<len(candidates) and candidates[index_next]==candidates[index]:
                index_next+=1
            answer(index_next,ds,target)
        answer(0,[],target)
        return ans