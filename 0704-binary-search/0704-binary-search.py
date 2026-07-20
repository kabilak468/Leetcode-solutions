class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            res=nums.index(target)
        else:
            res=-1
        return res        