class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution I came up myself: Chaining key-value pairs of
        # consecutive elements in the array. Make sure to start
        # counting ONLY when it is the start of a sequence
        hashmap = {}
        maxL = 0
        for i, num in enumerate(nums):
            if num in hashmap:
                continue
            else:
                hashmap[num] = num + 1
        for k, v in hashmap.items():
            if (k-1) in hashmap: 
                # Ensures that whatever has 
                # been seen would not be iterated through again
                continue
            else:
                length = 0
                curr = k
                while curr in hashmap:
                    curr = hashmap[curr]
                    length += 1
                if length > maxL:
                    maxL = length
        return maxL                    
                