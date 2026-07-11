class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        prev2 = 0

        for i in range(n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            not_pick = 0 + prev

            cur = max(pick, not_pick)
            prev2 = prev
            prev = cur
        
        return prev

        