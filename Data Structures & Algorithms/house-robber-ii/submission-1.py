class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        temp1, temp2 = [], []

        for i in range(n):
            if i != 0:
                temp1.append(nums[i])
            if i != n-1:
                temp2.append(nums[i]) 
        
        return max(self.houseRobber1(temp1), self.houseRobber1(temp2))
    
    def houseRobber1(self, nums):
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

        