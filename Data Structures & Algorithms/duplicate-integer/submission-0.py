class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if len(nums) != len(unique):
            return True
        else: 
            return False