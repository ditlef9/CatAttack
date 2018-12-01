class Board:

    def __init__(self, screenSizeX, screenSizeY):
        self.sizeX = int(4)
        self.sizeY = int(3)

# Positions, X, Y
def getPositionInPixels(pos):
    position = {
        "a1": (110, 110),
        "b1": (110, 260),
        "c1": (110, 410),
        "a2": (260, 210),
        "b2": (260, 260),
        "c2": (260, 410),
        "a3": (410, 210),
        "b3": (410, 260),
        "c3": (410, 410)
    }
    return position.get(pos)
