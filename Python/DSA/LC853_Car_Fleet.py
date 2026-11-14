class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # Sort cars by position in descending order
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        cur_time = 0

        # Process cars from nearest to the target
        for p, s in cars:

            # Calculate time needed to reach the target
            time = (target - p) / s

            # A new fleet forms if this car takes longer
            if time > cur_time:
                fleets += 1
                cur_time = time

        return fleets
      
