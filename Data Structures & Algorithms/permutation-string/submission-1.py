from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # naive approach: at every starting poing in s2, check
        # if s1 is there in permuted form.
        # O(n*m) 
        n = len(s1)
        m = len(s2)

        # what id like to do: a commutative rolling hash
        # where elements can be removed in O(1) and added in O(1)
        # then we can check in approach O(m+n), but guarantee is
        # hard to give
        if n > m: 
            return False
        
        diff = Counter(s1)

        #print(f'{diff=}')
        for i, c in enumerate(s2):
            diff[c] -= 1
            if diff[c] == 0:
                del diff[c]

            
            if i < n - 1: # nothing to do so far
                #print(f'post {i=} {c=} {diff=}')
                continue
            elif i == n - 1:
                if not diff:
                    return True
                continue

            oldchar = s2[i - n]
            diff[oldchar] += 1
            if diff[oldchar] == 0:
                del diff[oldchar]

            #print(f'post {i=} {c=} {diff=}')
            if not diff: # equal set
                return True

        return False






        