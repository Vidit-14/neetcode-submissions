class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1

        return sorted(hm, key=hm.get, reverse=True)[:k]
             
