import math
import os
import pygame

from Board import Board
from Piece import Piece
from Cat import Cat

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
        size = [screenSizeX, screenSizeY] # list
        self.screen = pygame.display.set_mode(size)
        
        # Title
        pygame.display.set_caption("Cat Attack!")
        
        #Loop until the user clicks the close button.
        self.done = False
        self.clock = pygame.time.Clock()
        
        # Create board
        self.bg = pygame.image.load("images/netherlands.jpg")
        
        # Game variables 
        self.gameWhosTurn = "red"
        self.gameCurrentActivePiece = ""
        
        # Game Board
        w, h = 3, 4;
        self.gameBoardPieces = [[0 for x in range(w)] for y in range(h)] 
        


        # Start game
        self.main()
        
    
    def main(self):
        # Pieces    
        self.pieceMonkeyBlue = Piece("blue", "monkey", "a1")
        self.pieceCatBlue = Piece("blue", "cat", "b1")
        self.pieceDogBlue = Piece("blue", "dog", "c1")
        self.pieceSheepBlue = Piece("blue", "sheep", "b2")
        self.pieceMonkeyRed = Piece("red", "monkey", "a4")
        self.pieceCatRed = Piece("red", "cat", "b4")
        self.pieceDogRed = Piece("red", "dog", "c4")
        self.pieceSheepRed = Piece("red", "sheep", "b3")
        
        self.gameBoardPieces[0][0] = "monkeyBlue"
        self.gameBoardPieces[0][1] = "catBlue"
        self.gameBoardPieces[0][2] = "dogBlue"
        self.gameBoardPieces[1][1] = "sheepBlue"
        
        self.gameBoardPieces[3][0] = "dogRed"
        self.gameBoardPieces[3][1] = "catRed"
        self.gameBoardPieces[3][2] = "monkeyRed"
        self.gameBoardPieces[2][1] = "sheepRed"
        
        
        
        while not self.done:
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            self.clock.tick(5)
             
             
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.done=True # Flag that we are done so we exit this loop

                if event.type == pygame.MOUSEBUTTONUP:
                    clickPositionPixelX, clickPositionPixelY = event.pos
                    
                    clickedOnPositionBoard = self.clickPositionPixelToPositionBoard(clickPositionPixelX, clickPositionPixelY)
                    clickedOnPiece = self.selectOrMovePiece(clickedOnPositionBoard)
                    
                    
                    
                    break
    
         
            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.
             
            # Clear the screen and set the screen background
            self.screen.fill((255, 255, 255))
        
            #INSIDE OF THE GAME LOOP
            self.screen.blit(self.bg, (0, 0))
                
            # Draw Board Xstart Ystart, Xstop, Ystop (diff is always 150 px)
            pygame.draw.rect(self.screen, self.colorYellow, [100, 100, 150, 150], 2) # A1
            pygame.draw.rect(self.screen, self.colorYellow, [100, 250, 150, 150], 2) # B1
            pygame.draw.rect(self.screen, self.colorYellow, [100, 400, 150, 150], 2) # C1
            
            pygame.draw.rect(self.screen, self.colorYellow, [250, 100, 150, 150], 2) # A2
            pygame.draw.rect(self.screen, self.colorYellow, [250, 250, 150, 150], 2) # B2
            pygame.draw.rect(self.screen, self.colorYellow, [250, 400, 150, 150], 2) # C2
            
            pygame.draw.rect(self.screen, self.colorYellow, [400, 100, 150, 150], 2) # A3
            pygame.draw.rect(self.screen, self.colorYellow, [400, 250, 150, 150], 2) # B3
            pygame.draw.rect(self.screen, self.colorYellow, [400, 400, 150, 150], 2) # C3
            
            pygame.draw.rect(self.screen, self.colorYellow, [550, 100, 150, 150], 2) # A4
            pygame.draw.rect(self.screen, self.colorYellow, [550, 250, 150, 150], 2) # B4
            pygame.draw.rect(self.screen, self.colorYellow, [550, 400, 150, 150], 2) # C4
            
            textsurface = self.fontArial.render('A', False, (0, 0, 0))
            self.screen.blit(textsurface,(70,175))
            
            textsurface = self.fontArial.render('B', False, (0, 0, 0))
            self.screen.blit(textsurface,(70,325))
            
            textsurface = self.fontArial.render('C', False, (0, 0, 0))
            self.screen.blit(textsurface,(70,475))
            
            textsurface = self.fontArial.render('1', False, (0, 0, 0))
            self.screen.blit(textsurface,(175,60))
            
            textsurface = self.fontArial.render('2', False, (0, 0, 0))
            self.screen.blit(textsurface,(325,60))
            
            textsurface = self.fontArial.render('3', False, (0, 0, 0))
            self.screen.blit(textsurface,(475,60))
            
            textsurface = self.fontArial.render('4', False, (0, 0, 0))
            self.screen.blit(textsurface,(625,60))
            
            
            # Draw pieces
            self.pieceMonkeyBlue.addPieceToBoard(pygame, self.screen)
            self.pieceCatBlue.addPieceToBoard(pygame, self.screen)
            self.pieceDogBlue.addPieceToBoard(pygame, self.screen)
            self.pieceSheepBlue.addPieceToBoard(pygame, self.screen)
        
            self.pieceMonkeyRed.addPieceToBoard(pygame, self.screen)
            self.pieceCatRed.addPieceToBoard(pygame, self.screen)
            self.pieceDogRed.addPieceToBoard(pygame, self.screen)
            self.pieceSheepRed.addPieceToBoard(pygame, self.screen)
        
            # Whos turn?
            if(self.gameWhosTurn == "red"):
                textsurface = self.fontArialH1.render('Reds turn', False, (0, 0, 0))
                self.screen.blit(textsurface,(800,20))
            elif(self.gameWhosTurn == "red"):
                textsurface = self.fontArialH1.render('Blues turn', False, (0, 0, 0))
                self.screen.blit(textsurface,(800,20))
                    
            
            # Draw
            pygame.display.flip()
         
        # Be IDLE friendly
        pygame.quit()
    
    #- Take some random position clicked and return the square (example a1) ---#
    def clickPositionPixelToPositionBoard(self, clickPositionPixelX, clickPositionPixelY):
        boardPositionX = ""
        boardPositionY = ""
        
        
        if(clickPositionPixelX > 100 and clickPositionPixelX < 250):
            boardPositionX = "1"
        elif(clickPositionPixelX > 250 and clickPositionPixelX < 400):
            boardPositionX = "2"
        elif(clickPositionPixelX > 400 and clickPositionPixelX < 550):
            boardPositionX = "3"
        elif(clickPositionPixelX > 550 and clickPositionPixelX < 700):
            boardPositionX = "4"
        else:
            boardPositionX = "-1"
    
        
        if(clickPositionPixelY > 100 and clickPositionPixelY < 250):
            boardPositionY = "a"
        elif(clickPositionPixelY > 250 and clickPositionPixelY < 400):
            boardPositionY = "b"
        elif(clickPositionPixelY > 400 and clickPositionPixelY < 550):
            boardPositionY = "c"
        elif(clickPositionPixelY > 550 and clickPositionPixelY < 700):
            boardPositionY = "d"
        else:
            boardPositionY = "Y Out of range", clickPositionPixelY
            
        xy = str(boardPositionY) + boardPositionX
        
        return xy
    
    
    #- Take some random square and give back what piece is in that square -----#
    # Also change the active state to the selected piece
    def selectOrMovePiece(self, clickedOnPositionBoard):
        
        # We either already have a piece active, or we are going to select a piece
        if(self.gameCurrentActivePiece == ""):
        
            # Set all inactive
            self.pieceMonkeyBlue.setActive("false")
            self.pieceCatBlue.setActive("false")
            self.pieceDogBlue.setActive("false")
            self.pieceSheepBlue.setActive("false")
            self.pieceMonkeyRed.setActive("false")
            self.pieceCatRed.setActive("false")
            self.pieceDogRed.setActive("false")
            self.pieceSheepRed.setActive("false")
            
            
            if(self.pieceMonkeyBlue.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "blue"):
                self.pieceMonkeyBlue.setActive("true")
                self.gameCurrentActivePiece = "monkeyBlue"
            elif(self.pieceCatBlue.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "blue"):
                self.pieceCatBlue.setActive("true")
                self.gameCurrentActivePiece = "catBlue"
            elif(self.pieceDogBlue.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "blue"):
                self.pieceDogBlue.setActive("true")
                self.gameCurrentActivePiece = "dogBlue"
            elif(self.pieceSheepBlue.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "blue"):
                self.pieceSheepBlue.setActive("true")
                self.gameCurrentActivePiece = "sheepBlue"
            if(self.pieceMonkeyRed.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "red"):
                self.pieceMonkeyRed.setActive("true")
                self.gameCurrentActivePiece = "monkeyRed"
            elif(self.pieceCatRed.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "red"):
                self.pieceCatRed.setActive("true")
                self.gameCurrentActivePiece = "catRed"
            elif(self.pieceDogRed.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "red"):
                self.pieceDogRed.setActive("true")
                self.gameCurrentActivePiece = "dogRed"
            elif(self.pieceSheepRed.getPosition() == clickedOnPositionBoard and self.gameWhosTurn == "red"):
                self.pieceSheepRed.setActive("true")
                self.gameCurrentActivePiece = "sheepRed"
            else:
                self.gameCurrentActivePiece = ""
            
            return self.gameCurrentActivePiece;
        
        else:
            print("Where do you want to move it?")
        
Main()