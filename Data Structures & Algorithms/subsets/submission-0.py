class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrackingDFS(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrackingDFS(i+1)

            subset.pop()
            backtrackingDFS(i+1)

        backtrackingDFS(0)
        return res