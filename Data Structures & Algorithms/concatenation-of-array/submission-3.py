class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j=len(nums)
        i=0
        ans=[0]*(2*j)
        for i in range(i,2*j):
            if i<j:
                ans[i]=nums[i]
            else:
                ans[i]=nums[i-j]
        return ans