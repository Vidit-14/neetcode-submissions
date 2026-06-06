class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        hashset = set()
        maxLen = 1
        if len(s) == 0:
            return 0
        else:
            hashset.add(s[l])

        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                maxLen = max(maxLen, (r-l+1))
                r += 1
            else:
                hashset.remove(s[l])
                l += 1

        return maxLen
        