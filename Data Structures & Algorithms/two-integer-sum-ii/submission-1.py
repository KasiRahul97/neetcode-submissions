class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)+1):
            for j in range(i+1,len(numbers)+1):
                if (numbers[i-1]+numbers[j-1]==target):
                    return [i,j]