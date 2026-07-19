class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums or len(nums)==0:
            return [-1,-1]
        else:
            ans=[]
            for i in range(len(nums)):
                if nums[i]==target:
                    ans.append(i)
            res=[]
            res.append(ans[0])
            res.append(ans[-1]) 
            return res          