import sys
from PySide import QtGui, QtCore
from card import *
from buttonCard import *

class Board(QtGui.QFrame):
    TYPE=1
    def __init__(self, parent,h,w,container):
        super(Board, self).__init__()
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        self.grid = QtGui.QGridLayout()
        self.container=container
        self.parent=parent
        self.initGui()
        self.setLayout(self.grid)
        self.cards=[]
        self.setStyleSheet("Board {background-image: url(pics/textureBoardb.png);}")
        
    def initGui(self):
        for i in range(7):
            for j in range(8):
                card =ButtonCard(self,QtGui.QPixmap("pics/c10.png"),self.parent,Board.TYPE) #this just initializes the pixmap
                card.setMaximumSize (100, 130)
                card.hide()
                self.grid.addWidget(card,i,j)
             
    '''
    changes all card images to unchosen
    '''   
    def unchoose(self):
        for card in self.cards:
            cont=True
            for i in range(7):
                for j in range(8):
                    if self.grid.itemAtPosition(i,j).widget().isVisible() and self.grid.itemAtPosition(i,j).widget().card==card:
                        self.grid.itemAtPosition(i,j).widget().setPic(self.container.getCard(card.getSuit(),card.getNumber()),card)
                        self.grid.itemAtPosition(i,j).widget().hide() #TODO:varmaan turha
                        self.grid.itemAtPosition(i,j).widget().show()
                        con=False
                        break
                if not cont:
                    break
        self.cards=[]
    
    '''
    changes unchosen card image to chosen card image and vice versa
    '''
    def choose(self,card):
        if card in self.cards:
            cont=True
            for i in range(7):
                for j in range(8):
                    if self.grid.itemAtPosition(i,j).widget().isVisible() and self.grid.itemAtPosition(i,j).widget().card==card:
                        self.grid.itemAtPosition(i,j).widget().setPic(self.container.getCard(card.getSuit(),card.getNumber()),card)
                        self.grid.itemAtPosition(i,j).widget().hide() #TODO:varmaan turha
                        self.grid.itemAtPosition(i,j).widget().show()
                        con=False
                        break
                if not cont:
                    break
            self.cards.remove(card)
            
        else:
            cont=True
            for i in range(7):
                for j in range(8):
                    if self.grid.itemAtPosition(i,j).widget().isVisible() and self.grid.itemAtPosition(i,j).widget().card==card:
                        self.grid.itemAtPosition(i,j).widget().setPic(self.container.getCardChosen(card.getSuit(),card.getNumber()),card)
                        self.grid.itemAtPosition(i,j).widget().hide() #TODO:varmaan turha
                        self.grid.itemAtPosition(i,j).widget().show()
                        con=False
                        break
                if not cont:
                    break
            self.cards.append(card)
            
                        
    '''
    update current board card images
    '''
    def update(self,cards):
        lkm=0
        for i in range(7):
            for j in range(8):
                self.grid.itemAtPosition(i,j).widget().hide()
                if lkm<len(cards):
                    card=cards[lkm]
                    self.grid.itemAtPosition(i,j).widget().setPic(self.container.getCard(card.getSuit(),card.getNumber()),card)
                    lkm+=1
                    if not self.grid.itemAtPosition(i,j).widget().isVisible():
                        self.grid.itemAtPosition(i,j).widget().show()
                else:
                    if self.grid.itemAtPosition(i,j).widget().isVisible():
                        self.grid.itemAtPosition(i,j).widget().hide()

