from hand import Hand

class Player(object):
    HUMAN = 1
    COMPUTER = 0
    
    def __init__(self,name,tyyppi):
        self.__name=name
        self.__cottages=0
        self.__points=0
        self.__hand = Hand()
        self.__type = tyyppi
        self.__stack = Hand()
        
    '''
    name methods
    '''
    def getName(self):
        return self.__name
        
    '''
    point methods
    '''
    def updatePoints(self,amount):
        self.__points += amount
        
    def setPoints(self,amount):
        self.__points = amount
        
    def getPoints(self):
        return self.__points
        
    '''
    cottage methods
    '''
    def getCottages(self):
        return self.__cottages  
        
    def raiseCottages(self,amount):
        self.__cottages+=amount
        
    def setCottages(self,amount):
        self.__cottages=amount
        
    def clearCottages(self):
        self.__cottages=0
        
    '''
    hand methods
    '''
    def getHand(self):
        return self.__hand
    
    def addCardsToHand(self,cards):
        self.__hand.addCards(cards)
            
    def addCardToHand(self,card):
        self.__hand.append(cards)
    
    def setHand(self,cards):
        self.__hand.clear()
        self.__hand.addCards(cards)
    
    def hasCards(self):
        return len(self.__hand.getCards())>0
    
    '''
    stack methods
    '''
    def getStack(self):
        return self.__stack
    
    def clearStack(self):
        self.__stack=Hand()
    
    def addCardsToStack(self,cards):
        for card in cards:
            self.addCardToStack(card)
            
    def addCardToStack(self,card):
        self.__stack.addCard(card)
    
    def setStack(self,cards):
        self.__stack.clear()
        self.__stack.addCards(cards)
    
    '''
    type methods
    '''
    def getType(self):
        return self.__type
            
    '''
    other methods
    '''
    def getScoreFromStack(self):
        points = self.__cottages
        points += self.__stack.getSureValue()
        return points
    
    def __str__(self):
        return self.__name+"-"+str(self.__points)
        

    
    
    
        
        