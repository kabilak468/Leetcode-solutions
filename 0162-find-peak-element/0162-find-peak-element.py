class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        arr=[]
        if nums[0]>nums[1]: 
            arr.append(nums[0])
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                arr.append(nums[i])
        if nums[-1]>nums[-2]:
            arr.append(nums[-1])        
        return nums.index(max(arr))