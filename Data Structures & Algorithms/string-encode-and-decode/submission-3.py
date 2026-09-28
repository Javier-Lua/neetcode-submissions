class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        return "".join(res)

    def decode(self, s: str) -> List[str]: # Read until the "#", if before it is a valid integer, read that amount of characters after the hashtag
        i, j = 0, 0
        res = []
        while i < len(s):
            if s[j] != "#":
                j += 1
                continue
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
            j = i
        return res
