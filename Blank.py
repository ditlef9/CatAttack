from Piece import Piece


class Blank(Piece):


    def __init__(self, color, name, icon, direction, position):
        self.color = color          # Blue or Red
        self.name = name            # Monkey, Cat, Dog or Sheep
        self.icon = icon            # dog_128_red
        self.isActive = False       # Is the icon should be active or not
        self.direction = direction  # 1 = Facing right, -1 = Facing left
        self.position = position    # Where on the board the piece is, is used for drawing only

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position