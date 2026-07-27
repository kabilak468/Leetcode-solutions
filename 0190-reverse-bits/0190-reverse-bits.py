class Solution:
    def reverseBits(self, n: int) -> int:
        b=format(n,'032b')
        s=str(b)[::-1]
        r=int(s,2)
        return r
