class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        n=0
        for x in b:
            if x=="1":
                n+=1
        return n        