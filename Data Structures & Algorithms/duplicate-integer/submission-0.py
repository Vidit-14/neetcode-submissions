class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set(nums)
        if len(s) == n:
            return False
        else: 
            return True
        