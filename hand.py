from card import Card
from deck import Deck

class Hand(object):
    def __init__(self):
        self.__cards = []
        
    def addCard(self,card):
        self.__cards.append(card)
    
    def addCards(self,cards):
        for card in cards:
            self.addCard(card)
        
    def removeCard(self,card):
        for i in self.__cards:
            if i == card:
                self.__cards.remove(i)
                return True
        return False
    
    def removeCards(self,cards):
        for i in cards:
            self.removeCard(i)
    
    def clear(self):
        self.__cards = []
    
    def getCards(self):
        return self.__cards
    
    def getAmountOfCards(self):
        return len(self.__cards)
    
    def getAmountOfSuit(self,suit):
        lkm=0
        for i in self.__cards:
            if i.getSuit()==suit:
                lkm+=1
        return lkm
    
    def getAmountOfNumber(self,number):
        lkm=0
        for i in self.__cards:
            if i.getNumber()==number:
                lkm+=1
        return lkm

    def hasCard(self,card):
        for i in self.__cards:
            if i==card:
                return True
        return False
    
    def getSureValue(self):
        points=0
        ruutu10 = Card(10,Card.DIAMONDS)
        pata2 = Card(2, Card.SPADES) 
        
        for i in self.__cards:
            if i==pata2:
                points+=1
            elif i==ruutu10:
                points+=2
            elif i.isNumber(Card.ACE):
                points+=1     
        return points
    
    def setCards(self,cards):
        self.clear()
        self.addCards(cards)
            






