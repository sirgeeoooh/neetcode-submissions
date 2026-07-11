class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest_count = 0
        current_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
                if current_count > highest_count:
                    highest_count = current_count
            else: 
                current_count = 0 
        
        return highest_count

        