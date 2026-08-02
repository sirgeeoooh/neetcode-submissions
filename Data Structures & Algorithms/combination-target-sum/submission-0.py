class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def backtrackingDFS(i,curList,total):
            if i >= len(nums) or total > target:
                return
            
            if total == target:
                res.append(curList.copy())
                return
            
            curList.append(nums[i])

            backtrackingDFS(i,curList,total + nums[i])
            curList.pop()
            backtrackingDFS(i+1,curList,total)
        
        backtrackingDFS(0,[],0)

        return res