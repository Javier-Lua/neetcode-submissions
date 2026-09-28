from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Create a hashmap where keys are 26-character tuples
        ## and values are the list of strings that represent the key
        hash = {}
        res = []
        for i, string in enumerate(strs):
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            temp = tuple(count)
            if temp in hash:
                hash[temp].append(string)
            else:
                hash[temp] = [string]
        for k, v in hash.items():
            res.append(v)
        return res
