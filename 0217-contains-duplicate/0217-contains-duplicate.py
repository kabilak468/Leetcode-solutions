class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        orig=list(set(nums))
        if len(orig)==len(nums):
            return False
        return True    