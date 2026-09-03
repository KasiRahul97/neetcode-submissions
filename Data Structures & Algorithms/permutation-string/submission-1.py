class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        l=0
        r=0
        while r < len2:
            r=l+len1-1
            if sorted(s2[l:r+1])==sorted(s1):
                return True
            else:
                l+=1
        return False       

