class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm=defaultdict(int)
        for i,num in enumerate(nums):
            cmplt=target-num
            if cmplt in hm:
                return [hm[cmplt],i]
            else:
                hm[num]=i
        return []