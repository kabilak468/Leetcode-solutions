class Solution:
    def firstUniqChar(self, s: str) -> int:
        orig=[]
        more=[]
        for x in s:
            if x not in orig:
                orig.append(x)
        for x in orig:
            if s.count(x)==1:
                return s.index(x)
                more.append(x)
        if not more:
            return -1
