class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(0,n+1):
            b=bin(i)[2:]
            arr.append(b)
        ans=[]
        for x in arr:
            c=x.count("1")
            ans.append(c)
        return ans                 