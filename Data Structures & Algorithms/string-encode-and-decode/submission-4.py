class Solution:
    # delimiter does not work because it might be confused with being part of the actual string
    def encode(self, strs: List[str]) -> str:
        # encoding has to contain length of each string after concatenation
        res = []
        for i, string in enumerate(strs):
            res.append(str(len(string)) + "#" + string)
        res = "".join(res)
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        temp = []
        i = 0
        while i < len(s):
            if s[i] != '#':
                temp.append(s[i])
                i += 1
            else:
                length = int("".join(temp))
                temp.clear()
                res.append(s[i + 1: i + length + 1])
                i = i + length + 1
        return res

