class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        max_length = 0
        length = 0

        for i in range(len(nums)):
            hm[nums[i]] = i

        for i in range(len(nums)):
            if (nums[i]-1) in hm:
                continue
            else:
                length = 1
                max_length = max(length, max_length)
                while (nums[i] + length) in hm:
                    length += 1
                    max_length = max(length, max_length)
            
        return max_length 
