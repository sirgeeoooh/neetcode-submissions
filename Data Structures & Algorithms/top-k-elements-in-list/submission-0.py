class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        res = [item[0] for item in counts.most_common(k)]

        return res
        
        