from tkinter import *
from random import *

# List of characters that determine block shape
blockList = ("t", "s", "z", "j", "l", "i", "o")
# List of block colors corresponding to the blocks above
colorList = ("yellow", "cyan", "green", "magenta", "blue", "orange", "red")

class TetrisGUI():
        def __init__(self):
                self.window = Tk()
                self.window.title("Tetris")
                self.window.geometry("240x540")

                self.page = Canvas(self.window, width=240, height=440, bg="black")
                self.page.pack()
                
                self.b1 = Button(self.window, text="Start", command=self.startGame)
                self.b1.place(x=100, y=480)

                # Place blue bars around tetris window
                self.page.create_rectangle(0, 0, 240, 19, fill="#696969", outline="#696969")
                self.page.create_rectangle(0, 421, 240, 440, fill="#696969", outline="#696969")
                self.page.create_rectangle(0, 20, 19, 420, fill="#696969", outline="#696969")
                self.page.create_rectangle(221, 20, 240, 420, fill="#696969", outline="#696969")

                # self.block is a single char that specifies the shape
                # t, s, z, j, l, i, o
                self.block = ""
                self.color = ""
                
                self.gameOvertxt = Label(self.window, text="Game Over")
                self.scoreWidget = Label(self.window)

                self.window.mainloop()
                
        def startGame(self):
                self.b1.config(text="Pause", command=self.pauseGame)
                self.gameOvertxt.place_forget()
                self.scoreWidget.place_forget()
                
                self.coordList = []
                self.activeBlockList = []
                self.score = 0
                self.pause = False

                self.createBlock()
                self.window.bind('<KeyPress>', self.keyPressed)
                self.moveBlock()

        def pauseGame(self):
                self.pause = True
                self.b1.config(text="Resume", command=self.resumeGame)

        def resumeGame(self):
                self.pause = False
                self.b1.config(text="Pause", command=self.pauseGame)
                self.window.bind('<KeyPress>', self.keyPressed)
                self.moveBlock()

        def createBlock(self):
                self.block = blockList[randint(0, 6)]
                self.color = colorList[blockList.index(self.block)]

                if self.block == "t":
                        self.page.create_rectangle(80, 20, 100, 40, fill=self.color)
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(120, 20, 140, 40, fill=self.color)
                        self.page.create_rectangle(100, 40, 120, 60, fill=self.color)
                        activeBlockList = [(80, 20), (100, 20), (120, 20), (100, 40)]

                elif self.block == "s":
                        self.page.create_rectangle(80, 40, 100, 60, fill=self.color)
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(120, 20, 140, 40, fill=self.color)
                        self.page.create_rectangle(100, 40, 120, 60, fill=self.color)
                        activeBlockList = [(80, 40), (100, 20), (120, 20), (100, 40)]
                        
                elif self.block == "z":
                        self.page.create_rectangle(80, 20, 100, 40, fill=self.color)
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(100, 40, 120, 60, fill=self.color)
                        self.page.create_rectangle(120, 40, 140, 60, fill=self.color)
                        activeBlockList = [(80, 20), (100, 20), (100, 40), (120, 40)]
                        
                elif self.block == "j":
                        self.page.create_rectangle(80, 20, 100, 40, fill=self.color)
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(120, 20, 140, 40, fill=self.color)
                        self.page.create_rectangle(120, 40, 140, 60, fill=self.color)
                        activeBlockList = [(80, 20), (100, 20), (120, 20), (120, 40)]
                        
                elif self.block == "l":
                        self.page.create_rectangle(80, 20, 100, 40, fill=self.color)
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(120, 20, 140, 40, fill=self.color)
                        self.page.create_rectangle(80, 40, 100, 60, fill=self.color)
                        activeBlockList = [(80, 20), (100, 20), (120, 20), (80, 40)]
                        
                elif self.block == "i":
                        self.page.create_rectangle(80, 20, 100, 40, fill=self.color)
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(120, 20, 140, 40, fill=self.color)
                        self.page.create_rectangle(140, 20, 160, 40, fill=self.color)
                        activeBlockList = [(80, 20), (100, 20), (120, 20), (140, 20)]
                        
                elif self.block == "o":
                        self.page.create_rectangle(100, 20, 120, 40, fill=self.color)
                        self.page.create_rectangle(120, 20, 140, 40, fill=self.color)
                        self.page.create_rectangle(100, 40, 120, 60, fill=self.color)
                        self.page.create_rectangle(120, 40, 140, 60, fill=self.color)
                        activeBlockList = [(100, 20), (120, 20), (100, 40), (120, 40)]
                        
                for activeBlockCoord in self.activeBlockList:
                        if self.coordList.contains(self.activeBlockCoord):
                                gameOver()
                
        def keyPressed(self, event):
                print()
        def moveBlock(self):
                print()
        def moveBlockLeft(self):
                print()
        def moveBlockRight(self):
                print()
        def gameOver(self):
                self.pause = True
                self.page.delete("activeBlock", "inactiveBlock")
                self.b1.confit(text="New Game", command=self.startGame)

TetrisGUI()
