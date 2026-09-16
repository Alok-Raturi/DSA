class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        test = {}
        for ind, i in enumerate(nums,start=1):
            com = target -i 
            if com in test:
                return [test[target-i]-1, ind-1]
            test[i] = ind