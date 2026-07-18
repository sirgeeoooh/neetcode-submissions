# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])
        return self.merge(left,right)

    
    def merge(self, left, right):
        res = []
        p1, p2 = 0,0
        l1, l2 = len(left), len(right)
        while p1 < l1 and p2 < l2:
            if left[p1].key <= right[p2].key:
                res.append(left[p1])
                p1 += 1
            else: 
                res.append(right[p2])
                p2 +=1
        return res + left[p1:] + right[p2:]