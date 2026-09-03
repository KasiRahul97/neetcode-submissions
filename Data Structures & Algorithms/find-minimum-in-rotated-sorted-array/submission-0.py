class Solution:
    def findMin(self, nums: List[int]) -> int:
        mins=100
        for i in nums:
            if i<mins:
                mins=i
        return mins