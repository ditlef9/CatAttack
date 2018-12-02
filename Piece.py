import Board


class Piece:
    

    def __init__(self, color, animal, position):
        self.color = color
        self.animal = animal
        self.position = position
        self.isActive = False
        self.imagePiece = ""
        
    
    
    def addPieceToBoard(self, pygame, screen):
        
        def getImagePath(animal, color, active=False):
            filename = "animals/" + animal + "_" + color + "_128"
            if (active):
                filename += "_active.png"
            else:
                filename += ".png"
            return filename

                
        # Image
        self.imagePiece = pygame.image.load(getImagePath(self.animal, self.color, self.isActive))

        # Positions, X, Y
        positionInPixels = Board.getPositionInPixels(self.position) #list
        
        
        
        screen.blit(self.imagePiece, positionInPixels)
        
 
    def getImage(self):
        return self.imagePiece
    
    def getPosition(self):
        return self.position
    
    def setActive(self, activeStatus):
        self.isActive = activeStatus