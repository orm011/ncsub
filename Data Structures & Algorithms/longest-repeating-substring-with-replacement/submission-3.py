class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # whats the longest single char substring in s, 
        # modulo making up to k replacements at my discretion.
        # related question:
        # what is the longest substring where at most k letters
        # are different from the rest.

        # initial thoughts
        # recursive structure? feels tricky.
        # eg, does the answer for s,k help us with s,k+1?
        #   feels like it may.
        # can we express the solution s,k in terms of 
        # smaller?
        #
        # lets think brute force: 
        # for any n C k set of k indices, flip them to 
        # the best value so that we get the longest substring possible. 

        # lets think of the problem s, 0
        # This is simply the longest single char substring.
        # now lets think of s, 1.  it may be equal to s,0
        # but if there are two runs of a symbol separated by a single
        # char, and these are long enough, then that would be the new
        # solution, 
        # eg. zzzzxxxyxxx. (s,0) = 4 (4zs)
        # but (s,1) = 7. (y->x , 7xs)

        # relation is not obvious from that.
        #
        # lets think of going left to right tracking longest.
        # Problem: i can use up one, but i may regret it later,
        # when that flip could have been better used, in retrospect.
        # ie, i may need to backtrack that decision


        # lets revisit the recursive approach:
        # suppose lets encode h,k the subproblem s[:h], k
        # if we know solutions for all <h, k
        # how do we express h, k. 
        # position h could be flipped. 
        # the solution for h,k-1 could be optimal, with the last
        # h adding or not.
        # with a last k used up at latest position. 
        # the solution for h-1, k, where we dont flip position h
        # at all. (but may still count)
        # is the last character part of the largest substring
        # if so we would find it if we always prefer longest
        # substring that ends latest, and we track that as well.

        # base case:
        # h = 0, k = 0: 0
        # h = 1, k = 0: 1 (single char)
        # h = 1, k = 1: 1 (single char)
        # h = 2, k = 0: 1 or 2 (depends)
        # h = 2, k = 1: 2 always, make them equal
        # h = 2, k = 2: 2 always.
        # h = 3, k = 0: 1 or 2 or 3.
        # h = 3, k = 1: look ak h = 2, k=1. that gives us 2. 
        #                 check if pos 2 is equal to second pos.
        #             (problem, we could have made a choice)
        # h = 3, k = 2: look at h = 2, k = 2
        #                 look at h = 2, k = 1. already gets you 2.
        #                 use that up for the lst.
        # h = 4, k = 0: find last
        # h = 4, k = 1: consider h = 3, k = 0. last string there.
        #                 then extend it with h = 4, k = 1 if possible.

        # the last char feels hard to pin down. we'd need some
        # concept of whether the char can change, or is fixed.

        # lets go back to longest substring idea base don 

        # lets define two pointers to define the substring
        #  we can expand the second
        # freely if it is the same as the prevous ones.
        # we get to cheat k times. then, the left pointer must move.
        # we need to track the whether we get a char back after moving, this requires use to track the characters we could use.

        # we could use a counter.
        window = Counter()

        i = 0
        j = 0 # position after last char.
        n = len(s)
        best = 0
        while j < n:
            # j - i is the number of elements.
            # after removing most common, we need to stay 
            # within k
            most_common = window.most_common(1)[0][1] if window else 0
            while j < n and j - i - most_common <= k:
                window[s[j]] += 1 # incr char
                j += 1 
                most_common = window.most_common(1)[0][1] if window else 0
                

            # undo last entry that exceeded k.
            if j - i - most_common > k:
                j -= 1
                window[s[j]] -= 1

            # record best right now
            best = max(best, j - i)
            # print(f"{(i,j)=} {most_common=} {best=} ")

            # now move left pointer once, see if we can 
            # move right again.
            if i < j:
                window[s[i]] -= 1
                i += 1

        return best
            


        
        




