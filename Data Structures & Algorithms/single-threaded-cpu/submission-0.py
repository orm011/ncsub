import heapq
import math

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # initial approach:
        # assume sorted by enqueue time
        # from among tasks with minimum enqueu time, 
        # pick smallest. 
        # increase time.
        # now from existing slice between last time and present,
        # pick min based first on completion time, and second on enqueue time.
        # tension between how the existing set of options depends
        # primarily on the their eqqueue time.
        # the optimal depends primarily on completion time
        if tasks == []:
            return []

        tasks_by_enqueue = sorted(zip(tasks, range(len(tasks))), 
        reverse=True) # reverse so we can pop 

        current_time = -math.inf
        possible_tasks = []
        ans = []
        while tasks_by_enqueue or possible_tasks:
            if tasks_by_enqueue and not possible_tasks and tasks_by_enqueue[-1][0][0] > current_time:
                # skip forward if idle time.
                current_time = tasks_by_enqueue[-1][0][0]
            
            # update possible tasks
            while tasks_by_enqueue:
                task = tasks_by_enqueue[-1]
                if task[0][0] <= current_time: # already enqueued
                    ((qtime, ptime), idx) = tasks_by_enqueue.pop()
                    heapq.heappush(possible_tasks, (ptime, qtime, idx))
                else:
                    break

            (next_task_ptime, next_task_qtime, next_task_idx) = heapq.heappop(possible_tasks)
            ans.append(next_task_idx) # record
            current_time += next_task_ptime #  process task
        return ans

            
                



            
            
            




