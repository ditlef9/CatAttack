import pygame

from Cat import Cat
from Dog import Dog
from Monkey import Monkey
from Sheep import Sheep


class Main:
    pygame.init()
    pygame.font.init()

    def __init__(self):

        # Initialize the game engine
        self.fontArialH1 = pygame.font.SysFont('Arial', 40)
        self.fontArial = pygame.font.SysFont('Arial', 30)

        # Define the colors we will use in RGB format
        self.colorYellow = (224, 196, 126)

        # Set the height and width of the screen
        screenSizeX = int(1080)
        screenSizeY = int(720)
        size = [screenSizeX, screenSizeY]  # list
        self.screen = pygame.display.set_mode(size)

        # Title
        pygame.display.set_caption("Cat Attack!")

        # Loop until the user clicks the close button.
        self.done = False
        self.clock = pygame.time.Clock()

        # Create board
        self.bg = pygame.image.load("images/netherlands.jpg")

        # Game variables 
        self.gameWhosTurn = "red"

        # Game Board
        self.gameboard = {}
        self.placePieces()
        w, h = 3, 4
        self.gameBoardPieces = [[0 for x in range(w)] for y in range(h)]


        # Start game
        self.main()

    #- Places pieces in array --------------------------------------------------------------------------------------- #
    def placePieces(self):

        self.gameboard[0, 0] = Monkey("red", "monkey", "monkey_red_128", 1, "a1");
        self.gameboard[0, 1] = Cat("red", "cat", "cat_red_128", 1, "b1");
        self.gameboard[0, 2] = Dog("red", "dog", "dog_red_128", 1, "c1");
        self.gameboard[1, 1] = Sheep("red", "sheep", "sheep_red_128", 1, "b2");

        self.gameboard[3, 0] = Monkey("blue", "monkey", "cat_blue_128", -1, "a4");
        self.gameboard[3, 1] = Cat("blue", "cat", "cat_blue_128", -1, "b4")
        self.gameboard[3, 2] = Dog("blue", "dog", "dog_blue_128", -1, "c4")
        self.gameboard[2, 1] = Sheep("blue", "sheep", "sheep_blue_128", -1, "b3")


    #- The game it self --------------------------------------------------------------------------------------------- #
    def main(self):

        while not self.done:
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            self.clock.tick(1)

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

                if event.type == pygame.MOUSEBUTTONUP:
                    clickPositionPixelX, clickPositionPixelY = event.pos

                    clickedOnPositionBoard = self.clickPositionPixelToPositionBoard(clickPositionPixelX,
                                                                                    clickPositionPixelY)
                    clickedOnPiece = self.selectOrMovePiece(clickedOnPositionBoard)

                    break



            # Clear the screen and set the screen background
            self.screen.fill((255, 255, 255))

            # INSIDE OF THE GAME LOOP
            self.screen.blit(self.bg, (0, 0))

            # Draw Board Xstart Ystart, Xstop, Ystop (diff is always 150 px)
            pygame.draw.rect(self.screen, self.colorYellow, [100, 100, 150, 150], 2)  # A1
            pygame.draw.rect(self.screen, self.colorYellow, [100, 250, 150, 150], 2)  # B1
            pygame.draw.rect(self.screen, self.colorYellow, [100, 400, 150, 150], 2)  # C1

            pygame.draw.rect(self.screen, self.colorYellow, [250, 100, 150, 150], 2)  # A2
            pygame.draw.rect(self.screen, self.colorYellow, [250, 250, 150, 150], 2)  # B2
            pygame.draw.rect(self.screen, self.colorYellow, [250, 400, 150, 150], 2)  # C2

            pygame.draw.rect(self.screen, self.colorYellow, [400, 100, 150, 150], 2)  # A3
            pygame.draw.rect(self.screen, self.colorYellow, [400, 250, 150, 150], 2)  # B3
            pygame.draw.rect(self.screen, self.colorYellow, [400, 400, 150, 150], 2)  # C3

            pygame.draw.rect(self.screen, self.colorYellow, [550, 100, 150, 150], 2)  # A4
            pygame.draw.rect(self.screen, self.colorYellow, [550, 250, 150, 150], 2)  # B4
            pygame.draw.rect(self.screen, self.colorYellow, [550, 400, 150, 150], 2)  # C4

            textsurface = self.fontArial.render('A', False, (0, 0, 0))
            self.screen.blit(textsurface, (70, 175))

            textsurface = self.fontArial.render('B', False, (0, 0, 0))
            self.screen.blit(textsurface, (70, 325))

            textsurface = self.fontArial.render('C', False, (0, 0, 0))
            self.screen.blit(textsurface, (70, 475))

            textsurface = self.fontArial.render('1', False, (0, 0, 0))
            self.screen.blit(textsurface, (175, 60))

            textsurface = self.fontArial.render('2', False, (0, 0, 0))
            self.screen.blit(textsurface, (325, 60))

            textsurface = self.fontArial.render('3', False, (0, 0, 0))
            self.screen.blit(textsurface, (475, 60))

            textsurface = self.fontArial.render('4', False, (0, 0, 0))
            self.screen.blit(textsurface, (625, 60))


            # Print board
            self.printBoard()


            # Draw
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()


    #- This method first prints the board to console, then print it to the board ------------------------------------ #
    def printBoard(self):

        # a) Print to console
        print("\n\n ")
        print("[0] 1 | [1] 2 | [2] 3 | [3] 4 ")

        itemA1 = self.gameboard.get((0, 0))
        itemA2 = self.gameboard.get((1, 0))
        itemA3 = self.gameboard.get((2, 0))
        itemA4 = self.gameboard.get((3, 0))
        print("[0] A", str(itemA1) + " | ", str(itemA2), " | ", str(itemA3), " | ", str(itemA4), " ")


        itemB1 = self.gameboard.get((0, 1))
        itemB2 = self.gameboard.get((1, 1))
        itemB3 = self.gameboard.get((2, 1))
        itemB4 = self.gameboard.get((3, 1))
        print("[1] B", str(itemB1) + " | ", str(itemB2), " | ", str(itemB3), " | ", str(itemB4), " ")

        itemC1 = self.gameboard.get((0, 2))
        itemC2 = self.gameboard.get((1, 2))
        itemC3 = self.gameboard.get((2, 2))
        itemC4 = self.gameboard.get((3, 2))
        print("[2] C", str(itemC1) + " | ", str(itemC2), " | ", str(itemC3), " | ", str(itemC4), " ")

        # b) Print to board
        for position,piece in self.gameboard.items():
            # print(type(piece), " ", piece.color, " ",  piece.name, " ",  piece.direction)
            # prints <class 'Sheep.Sheep'>   blue   sheep_blue_128   -1

            # Image
            filename = "animals/" + piece.icon + "" + ".png"
            imagePiece = pygame.image.load(filename)

            # Position is pixel
            positionInPixels = self.getPositionInPixels(piece.position)  # list

            self.screen.blit(imagePiece, positionInPixels)


    #- Positions, X, Y ---------------------------------------------------------------------------------------------- #
    # Takes in a position as "a1", "a2", etc and gives pixels back
    def getPositionInPixels(self, pos):
        position = {
            "a1": (110, 110),
            "b1": (110, 260),
            "c1": (110, 410),

            "a2": (260, 210),
            "b2": (260, 260),
            "c2": (260, 410),

            "a3": (410, 210),
            "b3": (410, 260),
            "c3": (410, 410),

            "a4": (560, 110),
            "b4": (560, 260),
            "c4": (560, 410),
        }
        return position.get(pos)




    # - Take some random position clicked and return the square (example a1) ------------------------------------------#
    # input = 100, 200,
    def clickPositionPixelToPositionBoard(self, clickPositionPixelX, clickPositionPixelY):
        boardPositionX = ""
        boardPositionY = ""

        if (clickPositionPixelX > 100 and clickPositionPixelX < 250):
            boardPositionX = "1"
        elif (clickPositionPixelX > 250 and clickPositionPixelX < 400):
            boardPositionX = "2"
        elif (clickPositionPixelX > 400 and clickPositionPixelX < 550):
            boardPositionX = "3"
        elif (clickPositionPixelX > 550 and clickPositionPixelX < 700):
            boardPositionX = "4"
        else:
            boardPositionX = "-1"

        if (clickPositionPixelY > 100 and clickPositionPixelY < 250):
            boardPositionY = "a"
        elif (clickPositionPixelY > 250 and clickPositionPixelY < 400):
            boardPositionY = "b"
        elif (clickPositionPixelY > 400 and clickPositionPixelY < 550):
            boardPositionY = "c"
        elif (clickPositionPixelY > 550 and clickPositionPixelY < 700):
            boardPositionY = "d"
        else:
            boardPositionY = "Y Out of range", clickPositionPixelY

        xy = str(boardPositionY) + boardPositionX

        return xy


    # - Take some random square and give back what piece is in that square -------------------------------------------#
    # input = a1, a2, a3, b1, etc
    def selectOrMovePiece(self, clickedOnPositionBoard):
        # Find the animal located at that position
        for position,piece in self.gameboard.items():
            # print(type(piece), " ", piece.color, " ",  piece.name, " ",  piece.direction)
            # prints <class 'Sheep.Sheep'>   blue   sheep_blue_128   -1

            if(piece.position == clickedOnPositionBoard):
                # piece.name = cat
                # piece.color = red

                # Change icon to active state
                piece.isActive = "true"



Main()
