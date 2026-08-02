class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:        
        times_left = [ (position_i, (target - position_i) / speed_i)   # assume continuous. 
         for (position_i, speed_i) in zip(position, speed) ]

        times_left.sort(reverse=True)
        actual_times = [times_left[0][1]]
        for i in range(1, len(position)):
            actual_times.append(max(times_left[i][1], actual_times[i-1]))
        
        return len(set(actual_times))