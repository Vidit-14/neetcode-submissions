class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = {}
        for c in s1:
            hm1[c] = hm1.get(c, 0) + 1
        
        l = 0
        r = 0
        hm2 = hm1.copy()

        while r < len(s2) and l < len(s2):
            if s2[r] not in hm2:
                l += 1
                r = l
                hm2 = hm1.copy()
            else:
                hm2[s2[r]] = hm2.get(s2[r], 0) - 1
                if hm2[s2[r]] == 0:
                    del hm2[s2[r]]
                r += 1

                if not hm2:
                    return True
        
        return False


        