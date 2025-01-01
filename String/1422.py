class Solution:
    def maxScore(self, s: str) -> int:
        t1=s.count('1')
        maxv=0
        c0=0
        c1=t1
        for i in range(len(s)-1):
            if s[i]=='0':
                c0+=1
            else:
                c1-=1
            cscore=c0+c1
            maxv=max(maxv,cscore)
        return maxv
