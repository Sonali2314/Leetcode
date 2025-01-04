class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        rcount = [0] * 26
        for char in s:
            rcount[ord(char) - ord('a')] += 1

        lseen = set()
        unique_palindromes = set()

        for char in s:
            rcount[ord(char) - ord('a')] -= 1
            for lchar in lseen:
                if rcount[ord(lchar) - ord('a')]:
                    unique_palindromes.add((lchar, char, lchar))
            lseen.add(char)

        return len(unique_palindromes)
