class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = sorted(list(zip(position, speed)), reverse=True)
        res = 0
        hours = 0
        for p, s in a:
            new_hours = (target - p) / s
            if new_hours > hours:
                res += 1
                hours = new_hours
        return res