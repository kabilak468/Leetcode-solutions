class Solution:
    def reverse(self, x: int) -> int:
        
        if x>=0:
            maxi=(2**31)-1
            num=int(str(x)[::-1])
            if num>maxi:
                num=0
        elif x<0:
            maxi=2**31
            num=-int(str(abs(x))[::-1])
            if num<-maxi:
                num=0       
        return num        