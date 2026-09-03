class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    if((i!=j)&(nums[i]+nums[j]==target)):
                        if(i>=j):
                            a.append(j)
                            a.append(i)
                        else:
                            a.append(i)
                            a.append(j)
        return a