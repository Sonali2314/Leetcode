class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel={'a','e','i','o','u'}
        valid=[]
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                valid.append(1)
            else:
                valid.append(0)
        psum=[0] * len(words)
        psum[0]=valid[0]
        for i in range(1,len(valid)):
            psum[i]=psum[i-1]+valid[i]
        ans=[]
        for li,ri in queries:
            if li==0:
                ans.append(psum[ri])
            else:
                ans.append(psum[ri]-psum[li-1])
        return ans
