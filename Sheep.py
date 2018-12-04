from Piece import Piece


class Sheep(Piece):

    def __init__(self, color, name, icon, direction, position):
        self.color = color          # Blue or Red
        self.name = name            # Monkey, Cat, Dog or Sheep
        self.icon = icon            # dog_128_red
        self.isActive = False       # Is the icon should be active or not
        self.direction = direction  # 1 = Facing right, -1 = Facing left
        self.position = position    # Where on the board the piece is, is used for drawing only

    def availableMoves(self, currentPos, wantedPos):
        x = currentPos[0]
        y = currentPos[1]
        x_new = wantedPos[0]
        y_new = wantedPos[1]

        one_forward_backward = (x + 1 == x_new or x - 1 == x_new) and y == y_new
        return one_forward_backward

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position