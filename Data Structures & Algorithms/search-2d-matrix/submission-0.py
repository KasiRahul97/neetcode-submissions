class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if matrix[j][i]==target:
                    return True
        return False