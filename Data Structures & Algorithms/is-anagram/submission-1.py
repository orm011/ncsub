class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        sc = [0 for i in range(30)]
        st = [0 for i in range(30)]

        offset = ord('a')
        for c in s:
            sc[ord(c) - offset] += 1

        for c in t:
            st[ord(c) - offset] += 1

        return sc == st