class Piece:
    
    def __init__(self, color, name, position):
        self.color = color
        self.name = name
        self.position = position
        self.isActive = ""
        self.imagePiece = ""
    
    
    def addPieceToBoard(self, pygame, screen):
        # Image
        if(self.color == "blue" and self.name == "monkey"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/monkey_blue_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/monkey_blue_128.png")
        elif(self.color == "blue" and self.name == "cat"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/cat_blue_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/cat_blue_128.png")
        elif(self.color == "blue" and self.name == "dog"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/dog_blue_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/dog_blue_128.png")
        elif(self.color == "blue" and self.name == "sheep"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/sheep_blue_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/sheep_blue_128.png")
            
        if(self.color == "red" and self.name == "monkey"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/monkey_red_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/monkey_red_128.png")
        elif(self.color == "red" and self.name == "cat"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/cat_red_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/cat_red_128.png")
        elif(self.color == "red" and self.name == "dog"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/dog_red_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/dog_red_128.png")
        elif(self.color == "red" and self.name == "sheep"):
            if(self.isActive == "true"):
                self.imagePiece = pygame.image.load("animals/sheep_red_128_active.png")
            else:
                self.imagePiece = pygame.image.load("animals/sheep_red_128.png")

        # Positions, X, Y
        if(self.position == "a1"):
            positionInPixels = (110,110) #list
        elif(self.position == "b1"):
            positionInPixels = (110,260) #list
        elif(self.position == "c1"):
            positionInPixels = (110,410) #list
            
        elif(self.position == "a2"):
            positionInPixels = (260,210) #list
        elif(self.position == "b2"):
            positionInPixels = (260,260) #list
        elif(self.position == "c2"):
            positionInPixels = (260,410) #list
            
        elif(self.position == "a3"):
            positionInPixels = (410,210) #list
        elif(self.position == "b3"):
            positionInPixels = (410,260) #list
        elif(self.position == "c3"):
            positionInPixels = (410,410) #list
            
        elif(self.position == "a4"):
            positionInPixels = (560,110) #list
        elif(self.position == "b4"):
            positionInPixels = (560,260) #list
        elif(self.position == "c4"):
            positionInPixels = (560,410) #list
        
        
        
        screen.blit(self.imagePiece, positionInPixels)
        
 
    def getImage(self):
        return self.imagePiece
    
    def getPosition(self):
        return self.position
    
    def setActive(self, activeStatus):
        self.isActive = activeStatus