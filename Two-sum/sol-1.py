class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for ind, i in enumerate(nums):
            sliced = nums[ind+1:]
            for index, j in enumerate(sliced):
                if i+j == target:
                    return [ind, index+ind+1]
        