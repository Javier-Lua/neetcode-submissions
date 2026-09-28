class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array in ascending order, then fix an element in
        # the array, and run sorted 2sum 2-pointers on the remaining
        # elements after it. Do this for every non-duplicate element
        # in the array. Sorting helps with easier duplicate handling,
        # don't have to worry about swapped numbers and can just skip
        # if previous == next.
        nums = sorted(nums)
        pointer = 0
        res = []
        while pointer < len(nums):
            if (pointer > 0 and nums[pointer] == nums[pointer - 1]):
                pointer += 1
                continue
            minires = self.twoSum(nums, pointer + 1, nums[pointer])
            if minires != []:
                res.extend(minires)
            pointer += 1
        return res
    
    def twoSum(self, nums, left, target):
        p1, p2 = left, len(nums) - 1
        res = []
        while p1 < p2:
            if (nums[p1] + nums[p2] == -target):
                res.append([nums[left - 1], nums[p1], nums[p2]])
                while (p1 < len(nums) - 1 and nums[p1 + 1] == nums[p1]):
                    p1 += 1
                while (p2 > 0 and nums[p2 - 1] == nums[p2]):
                    p2 -= 1
            if (nums[p1] + nums[p2] < -target):
                p1 += 1
            else:
                p2 -= 1
        return res