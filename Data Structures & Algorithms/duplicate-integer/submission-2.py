class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cpy=nums
        
        for i in nums:
            count=0
            for j in cpy:
                if i==j:
                    count=count+1
                    if count>1:
                        return True
                        break
                    else:
                        continue
        return False
