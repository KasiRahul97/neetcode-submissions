class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count=0
        for ch in nums:
            if ch==target:
                return count
            else:
                count+=1
        return -1