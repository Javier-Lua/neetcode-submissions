class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Generate prefix and postfix multiplication array
        prefix, postfix = nums.copy(), nums.copy()
        for i in range(len(nums)):
            if i > 0:
                prefix[i] *= prefix[i - 1]
            if i > 1:
                postfix[-i] *= postfix[-i + 1]
        postfix[0] *= postfix[1]
        res = [0 for _ in range(len(nums))]
        for i in range(len(res)):
            if i > 0 and i < len(res) - 1:
                res[i] = prefix[i - 1] * postfix[i + 1]
            else:
                if i == 0:
                    res[i] = postfix[i + 1]
                else:
                    res[i] = prefix[i - 1]
        return res
