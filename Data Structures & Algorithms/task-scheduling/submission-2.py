class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if a task X appears k times, we will need at least 
        # (1 + n) * (k - 1) + 1 slots.
        # we can use up the rest of the slots with other stuff.
        # we could pick the task with the largest count,
        # then fill the gaps with the second largest count
        # and so on, until one of two things happens:
        # n is big enough (there are fewer or equal to n + 1 tasks)
        # or we need to place some left over tasks in later slots.
        # or we push the repetitions a bit beyond n to accomodate.
        
        # idea: greedy.
        # track which is the leftover tasks with greatest "critical path"
        # (longest reps) and is currently enabled to run
        # track: (task name, last time scheduled, remaining reps)
        # order by 
        # a. last time scheduled (desc, enabled goes first), 
        # b. remaining reps (desc also)
        # then we update last time scheduled and count...

        # which structure can we use to quickly figure track the
        # next best task to run?
        # a doubly linked list that we keep in order is one option.
        # but we need to figure out its position


        # but we can only schedule one at a time, so last time scheduled
        # is always unique, and always going to be at the extreme...
        
        # start:
        # order queue by least reps to most reps.
        # pick entry, decrease reps by one, now goes to back of the queue.
        # with decreased count.
        # as we do this, count keeps decreasing for everything,
        # so the relative ordering is constant.
        # but eventually we may find multiple enabled options (bc time passed)
        # but the head of the queue has much fewer reps tahn something 
        # in the middle.
        # we want to find the largest reps remaining enabled.

        # enabled tasks: stay in max heap (by count, largest is top)
        # disabled tasks: stay in min heap (by time, earliest is top)

        # at every step: 
        # increase time by 1.
        #  if there are newly enabled tasks, move them to enabled heap with count.
        # pick the max from the heap
        # pass it back to disabled with the current time and decreased count
        # 
        # if there are no newly enabled tasks, just work with already enabled.
        # if there are neighter, increase time to the first enabled one.
        from collections import Counter
        import heapq

        counts = Counter(tasks)
        enabled = [(-c,k) for (k,c) in counts.items()] # max heap on remaining steps
        heapq.heapify(enabled)
        disabled = [] # min heap on time
        # (last, count, name)

        time = 0
        record = []
        while enabled or disabled:
            if not enabled: # jump forward to just before
                time = disabled[0][0] + n
            else:
                pass
                # already something possible, just account for time

            time += 1 # one step

            if disabled and disabled[0][0] + n < time:
                (_, ecount, ename) = heapq.heappop(disabled)
                heapq.heappush(enabled, (ecount, ename))
            
            
            assert enabled
            (negcount, name) = heapq.heappop(enabled)
            if negcount + 1 < 0:
                heapq.heappush(disabled, (time, negcount + 1, name))

        return time





