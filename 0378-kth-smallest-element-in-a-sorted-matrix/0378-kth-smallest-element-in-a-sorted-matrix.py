class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr=[]
        for x in matrix:
            for y in x:
                arr.append(y)
        arr.sort()
        return arr[k-1]