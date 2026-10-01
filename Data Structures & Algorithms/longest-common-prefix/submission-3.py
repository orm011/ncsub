class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        slen = min([len(s) for s in strs])

        prev = None
        broke = False
        n = len(strs)

        nstrs = 0
        for i in range(slen):
            for (j,s) in enumerate(strs):
                if j == 0:
                    prev = s[i]

                if s[i] != prev:
                    broke = True
                    break

                nstrs += 1
            
            if broke:
                break # :i will exclude this one

        rounds, left = divmod(nstrs, n)
        return strs[0][:rounds]

