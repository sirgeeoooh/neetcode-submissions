"""
target - p1 = key in dict

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]

            if complement in complements:
                return [complements[complement],i]
            else:
                complements[nums[i]] = i
            