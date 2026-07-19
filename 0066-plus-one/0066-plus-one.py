class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for x in digits:
            s+=str(x)
        num=str(int(s)+1)
        lst=[]
        for x in num:
            lst.append(int(x))
        return lst    