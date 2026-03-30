class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # init pos
        # hours taken to reach target
        cars = sorted(zip(position, speed), reverse = True)
        fleets = []
        for pos, spd in cars:
            hours = (target - pos) / float(spd)
            indivFleet = True
            for i in range(len(fleets)):
                p, h = fleets[i][0], fleets[i][1]
                if (p >= pos and h >= hours or
                    p <= pos and h <= hours):
                    fleets[i][0] = max(p, pos)
                    fleets[i][1] = max(h, hours)
                    indivFleet = False
                    break
            if indivFleet:
                fleets.append([pos, hours])
            print(fleets)
        return len(fleets)