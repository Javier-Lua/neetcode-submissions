class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i, x in enumerate(nums):
            hash.update({x : i})
        for j, num in enumerate(nums):
            complement = target - num
            ## Iterate through the array so if there are duplicate keys,
            ## it will be taken into account, as the array has both dup keys
            if complement in hash and j != hash[complement]:
                return [j, hash[complement]]
        return []

    """
    First attempt
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
    """
