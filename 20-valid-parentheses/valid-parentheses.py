class Solution:
    def isValid(self, s: str) -> bool:
        matchdict={
            '(':')',
            '[':']',
            '{':'}'
        }
        l=[]
        for i in range(len(s)):
            if s[i] in matchdict:
                l.append(s[i])
            else:
                if len(l)==0:
                    return False
                if s[i]==matchdict[l[-1]]:
                    l.pop()
                else:
                    return False
        return len(l)==0
