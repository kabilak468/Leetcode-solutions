class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        lst=sentence.split()
        d=discount/100
        arr=[]
        for x in lst:
            if x[0]=="$" and len(x[1:])>0 and x[1:].isdigit():
                p=int(x[1:])
                dis=p*d
                res=p-dis
                arr.append(str(f"${res:.2f}")) 
            else:
                arr.append(x)
        return " ".join(arr)            