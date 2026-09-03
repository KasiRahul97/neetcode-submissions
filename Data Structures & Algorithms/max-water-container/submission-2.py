class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most=0
        l=0
        r=len(heights)-1
        while l<r:
            curr=min(heights[l],heights[r])*(r-l)
            most=max(most,curr)
            if heights[l]<=heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
        return most