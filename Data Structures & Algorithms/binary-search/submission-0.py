class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1
        loc = -1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                loc = mid
                return loc
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return loc        