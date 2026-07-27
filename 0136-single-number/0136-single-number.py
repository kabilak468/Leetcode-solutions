class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single=list(set(nums))
        n=len(single)
        freq=[]
        for i in range(n):
            r=nums.count(single[i])
            freq.append(r)
        dic=dict(zip(single,freq))
        for k,v in dic.items():
            if v==1:
                return k