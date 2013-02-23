from random import shuffle
from card import Card

class Deck(object):
    
    def __init__(self):
        self.__cards=[]
        
        for i in range(1,14):
            for j in range(4):
                card = Card(i,j)
                self.__cards.append(card)
        self.shuffle()
        
    def shuffle(self):
        shuffle(self.__cards)
        
    def deal(self,amount):
        cardsToDeal=[]
        for i in range(amount):
            if len(self.__cards)==0:
                break
            cardsToDeal.append(self.__cards.pop())
        return cardsToDeal
    
    def getCards(self):
        return self.__cards
    
    def cardsLeft(self):
        return len(self.__cards)
    
    def setCards(self,cards):
        self.__cards=cards




