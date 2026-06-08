class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        hm = {}
        res = []

        while r < k:
            hm[r] = hm.get(r, nums[r])
            r += 1
        
        maxKey = max(hm, key = hm.get)
        res.append(nums[maxKey])
        del hm[l]
        l += 1

        while r < len(nums):
            hm[r] = hm.get(r,nums[r])
            maxKey = max(hm, key = hm.get)
            res.append(nums[maxKey])
            r += 1
            del hm[l]
            l += 1
        
        return res


        