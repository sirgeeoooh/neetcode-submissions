class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        elements_right = []
        for i in range(len(arr)):
            elements_right = arr[i+1:]
            if len(elements_right) == 0:
                arr[i] = -1
            else:
                arr[i] = max(elements_right)
        
        return arr