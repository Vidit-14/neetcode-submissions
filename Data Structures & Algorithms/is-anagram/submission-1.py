class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        for ch in s:
            hm[ch] = hm.get(ch, 0) + 1
        
        for ch in t:
            hm[ch] = hm.get(ch, 0) - 1
            if hm[ch] == 0:
                del hm[ch]
        
        if not hm:
            return True
        else:
            return False
        