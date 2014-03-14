import sys
from PyQt4 import QtGui, QtCore
from card import *
from buttonCard import *
from player import *

class HandPlr(QtGui.QFrame):
    TYPE=0
    def __init__(self, parent,h,w,container):
        super(HandPlr, self).__init__()
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        self.container=container
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        self.parent=parent
        self.chosenCard=None
        self.cards=[]

        for i in range(4):
            card =ButtonCard(self,QtGui.QPixmap("pics/c10.png"),self.parent,HandPlr.TYPE)#TODO:
            card.setMaximumSize (100, 130)
            card.hide()
            self.grid.addWidget(card,1,i)
        self.setLayout(self.grid)
        self.setStyleSheet("HandPlr {background-image: url(pics/textureHandb.png);}")
    
    def unchoose(self):
        if self.chosenCard!=None:
            for i in range(4):
                if self.grid.itemAtPosition(1,i).widget().isVisible() and self.grid.itemAtPosition(1,i).widget().card==self.chosenCard:
                    self.grid.itemAtPosition(1,i).widget().setPic(self.container.getCard(self.chosenCard.getSuit(),self.chosenCard.getNumber()),self.chosenCard)
                    self.grid.itemAtPosition(1,i).widget().hide()
                    self.grid.itemAtPosition(1,i).widget().show()
        self.chosenCard=None
    
    def choose(self,card):
        if self.chosenCard!=None:
            for i in range(4):
                if self.grid.itemAtPosition(1,i).widget().isVisible() and self.grid.itemAtPosition(1,i).widget().card==self.chosenCard:
                    self.grid.itemAtPosition(1,i).widget().setPic(self.container.getCard(self.chosenCard.getSuit(),self.chosenCard.getNumber()),self.chosenCard)
                    self.grid.itemAtPosition(1,i).widget().hide()
                    self.grid.itemAtPosition(1,i).widget().show()
                    
        self.chosenCard=card            
        for i in range(4):
            if self.grid.itemAtPosition(1,i).widget().isVisible() and self.grid.itemAtPosition(1,i).widget().card==card:
                self.grid.itemAtPosition(1,i).widget().setPic(self.container.getCardChosen(self.chosenCard.getSuit(),self.chosenCard.getNumber()),self.chosenCard)
                self.grid.itemAtPosition(1,i).widget().hide()
                self.grid.itemAtPosition(1,i).widget().show()
        
                
        
    def update(self,cards,type):
        lkm=0
        self.cards=cards
        for i in range(4):
            self.grid.itemAtPosition(1,i).widget().hide()
            if lkm<len(cards):
                    card=cards[lkm]
                    if type == Player.HUMAN:
                        self.grid.itemAtPosition(1,i).widget().setPic(self.container.getCard(card.getSuit(),card.getNumber()),card)
                    else:
                        self.grid.itemAtPosition(1,i).widget().setPic(self.container.getBack(),card)
                    lkm+=1
                    if not self.grid.itemAtPosition(1,i).widget().isVisible():
                        self.grid.itemAtPosition(1,i).widget().show()
            else:
                if self.grid.itemAtPosition(1,i).widget().isVisible():
                    self.grid.itemAtPosition(1,i).widget().hide()
