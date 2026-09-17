class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        
        for ind, i in enumerate(nums):
            if i in window: 
                return True
            window.add(i)
            if len(window) > k:
                window.remove(nums[ind-k])
        return False