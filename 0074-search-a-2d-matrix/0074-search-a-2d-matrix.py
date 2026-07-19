class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for x in matrix:
            for y in x:
                arr.append(y)
        return target in arr        