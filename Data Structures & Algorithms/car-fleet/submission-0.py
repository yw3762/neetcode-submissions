class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # two remarks:
        # 1. if two cars say 1, 2, with pos1 < pos2, eventually meet,
        #    then they will become one fleet. So we could scan from higher
        #    pos down to lower pos, use the highest as reference.
        # 2. if one lower pos car don't catch up to the highest pos, then
        #    we could conclude that it's a fleet by itself and update 
        #    higher pos to it.

        cars = sorted(zip(position, speed), reverse=True)

        fleet_time = -1
        count = 0
        for pos, spd in cars:
            arrival = (target - pos) / spd
            if arrival > fleet_time:
                count += 1
                fleet_time = arrival
                
        return count