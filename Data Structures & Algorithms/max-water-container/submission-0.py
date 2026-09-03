class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most=0
        for i in range(len(heights)):
            curr=0
            for j in range(i+1,len(heights)):
                curr=min(heights[i],heights[j])*(j-i)
                most=max(most,curr)
        return most

