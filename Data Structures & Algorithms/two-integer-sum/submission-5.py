class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return False'''
        d=defaultdict(int)
        for i,num in enumerate(nums):
            s=target-num
            if s in d:
                return [d[s],i]
            else:
                d[num]=i
        return False