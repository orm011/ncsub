class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counts = [0 for _ in range(26)]
        offset = ord('A')
        mostfreq = 0
        for t in tasks:
            pos = ord(t) - offset
            counts[pos] += 1
            mostfreq = max(mostfreq, counts[pos])
        
        freqs = Counter(counts)
        del freqs[0] # count 0  
        # how many tasks have each count
        
        # solution will take the m largest counts and schedule 
        # those. then schedule the m + m
        f = mostfreq
        m = freqs[mostfreq]
        #print(f"{f=} {m=}")
        T = len(tasks)
        return max(T, (f - 1) * (n + 1) + m)
        
