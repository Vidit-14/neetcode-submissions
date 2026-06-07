class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        hm = {}
        hm[s[l]] = hm.get(s[l], 0) + 1
        maxLen = 1

        while r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            freq = max(hm, key = hm.get)
            
            if ((r-l+1) - hm[freq]) > k:
                hm[s[l]] = hm.get(s[l], 0) - 1
                l += 1
                r += 1
            else:
                maxLen = max(maxLen, r-l+1)
                r += 1

        return maxLen        