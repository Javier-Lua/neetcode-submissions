from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        if len(s) < 2:
            return len(s)
        left = 0
        right = 0
        unique_chars = Counter()
        unique_chars[s[right]] += 1
        max_length = 1
        curr_length = 1
        while right < len(s) - 1:
            right += 1
            while s[right] in unique_chars:
                del unique_chars[s[left]]
                left += 1
            unique_chars[s[right]] += 1
            curr_length = right - left + 1
            max_length = max(max_length, curr_length)
        return max_length
        


