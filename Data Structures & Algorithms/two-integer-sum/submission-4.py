class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i, x in enumerate(nums):
            if x in hash and target == x + x:
                return [hash[x][1], i]
            else:
                hash.update({x : (target - x, i)})
        for key, value in hash.items():
            if value[0] in hash and value[1] != hash[value[0]][1]:
                return [value[1], hash[value[0]][1]]
