class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # simple approach 1: 
        # apply updates at every step.
        # step one lets sort the positions. we know the relative order will never change.
        # move every car_i to position min(pos_i + speed_i, pos_i+1) at the next step.
        
        steps_left = [ target - pos for pos in position ]
        times = [(steps_left / speed)  # assume continuous. 
         for (steps_left, speed) in zip(steps_left, speed) ]

        sorted_pairs = sorted(zip(position, times), reverse=True) # highest position closest to 0
        sorted_pos = [pos for (pos,_) in sorted_pairs]
        times_remaining = [time for (_, time) in sorted_pairs]
        actual_times = [times_remaining[0]]
        for i in range(1, len(position)):
            actual_times.append(max(times_remaining[i], actual_times[i-1]))
        
        return len(set(actual_times))