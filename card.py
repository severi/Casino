

'''
This is used when loading a game from a text file
'''
def makeCard(str):
    suit=int(str[0])
    
    num=0
    if str[1]=='T':
        num=10
    elif str[1]=='J':
        num=11
    elif str[1]=='Q':
        num=12
    elif str[1]=='K':
        num=13
    else:
        num=int(str[1])
    
    card = Card(num,suit)
    return card

class Card(object):
    DI10 = 8.0 #ruutu10
    SP2 = 7.0 #pata2
    AC = 6.0 #assa
    SPAD = 0.1 #pata
    BASIC = 0.5

    SPADES = 0
    CLUBS = 1
    HEARTS = 2
    DIAMONDS = 3
    ACE = 1
    JACK=11
    QUEEN = 12
    KING = 13
    
    def __init__(self,num,sui):
        self.__number = num
        self.__suit = sui
        self.__handValue = num  #cards value in players hand
        self.__boardValue = num #cards value on board
        self.__compValue = Card.BASIC #valuation for card used in valuating cards in playComputerTurn
        
        if num==Card.ACE:
            self.__handValue = 14
            self.__compValue += Card.AC
            
        if num==10 and sui == Card.DIAMONDS:
            self.__handValue=16
            self.__compValue += Card.DI10
            
        if num==2 and sui == Card.SPADES:
            self.__handValue = 15
            self.__compValue += Card.SP2
            
        if sui == Card.SPADES:
            self.__compValue += Card.SPAD
            
    def isSuit(self,suit):
        return self.__suit==suit
    
    def isNumber(self,number):
        return self.__number==number
    
    def getSuit(self):
        return self.__suit
    
    def getNumber(self):
        return self.__number
    
    def getHandValue(self):
        return self.__handValue
    
    def getBoardValue(self):
        return self.__boardValue
    
    def getCompValue(self):
        return self.__compValue
    
    
    '''
    get card as string used when saving the game
    '''
    def cardSave(self):
        suit=''
        num=''
        if self.__number==10:
            num='T'
        elif self.__number==11:
            num='J'
        elif self.__number==12:
            num='Q'
        elif self.__number==13:
            num='K'
        else:
            num=str(self.__number)
        suit=str(self.__suit)
        txt=suit+num
        return txt
    
    
    '''
    overridden operators
    '''
    def equals(self, other):
        return self == other

    def __lt__(self, other):
        return self.getNumber()<other.getNumber()
    
    def __gt__(self, other):
        return self.getNumber()>other.getNumber()
    
    def __le__(self, other):
        return self.getNumber()<=other.getNumber()
    
    def __ge__(self, other):
        return self.getNumber()>=other.getNumber()
    
    def __eq__(self, other):
        if other==None:
            sama=False
        else:
            sama=self.__number == other.getNumber() and self.__suit == other.getSuit()
        return sama

    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        if self.__suit==Card.SPADES:
            suit=" of SPADES"
        elif self.__suit==Card.CLUBS:
            suit=" of CLUBS"
        elif self.__suit==Card.HEARTS:
            suit=" of HEARTS"
        else:
            suit=" of DIAMONDS"
        return str(self.__number)+suit
    

    
        