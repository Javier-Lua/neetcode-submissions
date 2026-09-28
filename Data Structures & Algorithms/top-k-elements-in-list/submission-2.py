from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        # bucket[i] contains elements with frequency i
        for key, v in freq.items():
            bucket[v].append(key)
        for i in range(-1, -len(bucket), -1):
            if not bucket[i]:
                continue
            else:
                for j in range(len(bucket[i])):
                    res.append(bucket[i][j])
                    if len(res) == k:
                        return res