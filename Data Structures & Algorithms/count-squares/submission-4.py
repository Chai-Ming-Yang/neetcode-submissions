class CountSquares:

    def __init__(self):
        self.visX = defaultdict(set)
        self.visY = defaultdict(set)
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.visX[x].add(y)
        self.visY[y].add(x)
        self.freq[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        x_to_y, y_to_x = list(self.visX[x]), list(self.visY[y])
        res = 0
        for ny in x_to_y:
            for nx in y_to_x:
                if ny == y and nx == x: continue
                if (ny in self.visX[nx] and nx in self.visY[ny] and 
                    abs(ny-y) == abs(nx-x)): 
                    res += self.freq[(nx, ny)] * self.freq[(nx, y)] * self.freq[(x, ny)]
                    
        return res