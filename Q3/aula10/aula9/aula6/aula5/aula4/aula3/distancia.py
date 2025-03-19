def dist (x1: float, x2: float, x3: float, y1: float, y2: float, y3: float) -> float:
    return ((x1 - y1) ** 2 + (x2 - y2) ** 2 + (x3 - y3) ** 2) ** 0.5
