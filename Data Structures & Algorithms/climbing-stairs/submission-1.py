class Solution:
    def climbStairs(self, n: int) -> int:
        #n = 5
        curr, prev = 1, 1
        # 4 , 5    = 1, 1

        for i in range(n-2, -1, -1): # from (3 to 0)
            temp = curr
            curr = curr + prev
            prev = temp
        
        return curr