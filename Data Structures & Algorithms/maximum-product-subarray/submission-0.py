class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            best=nums[0]
            worst=nums[0]
            global_best=nums[0]
            candidates=[nums[0],best,worst]
            for num in nums[1:]:
                candidates=[num,best*num,worst*num]
                best=max(candidates)
                worst=min(candidates)
                global_best=max(global_best,best)
            return global_best

                
