class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*(len(nums))
        for i in range(0,len(nums)):
            count=1
            if i==0:
                for j in range(i+1,len(nums)):
                    count=count*nums[j]
            else:
                for j in range(0,i):
                    count=count*nums[j]
                for j in range(i+1,len(nums)):
                    count=count*nums[j]
            res[i]=count
        return res