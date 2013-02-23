from card import Card
from itertools import combinations
from player import Player
from game import Game

'''
validRaise-functions
'''

'''
used in gameLogic's validRaise-function

this function returns the possible card groups to raise based on the value of the raiseCard
param: raiseCardValue, cardsToRaise
return:possible combinations to raise
'''
def getValidGroups1(value, cards):
    valid = []
    for i in range(1,len(cards)+1):
        comb = combinations(cards,i)
        for j in comb:
            summa=0
            for z in j:
                summa+=z.getBoardValue()
            if summa==value:
                valid.append(j)
    return valid

'''
used in gameLogic's validRaise-function

This function takes groups as parameter,makes combinations of them and returns those, whose length(card amount) is the same as that of the cards the player wants to raise

param: number of cards to raise, possible card groups
return:groups of card groups, whose length is the same as that of the cards to raise
'''
def getValidGroups2(length,groups):
    valid = []
    for i in range(1,len(groups)+1):
        comb = combinations(groups,i)
        for j in comb:
            summa=0
            for z in j:
                summa+=len(z)
            if summa==length:
                valid.append(j)
    return valid

'''
used in gameLogic's validRaise-function

returns groups that has all the cards, that player wants to raise, in it.

param: cardsToRaise, possible card groups with correct length
return:groups, that include all the wished cards
'''
def getValidGroups3(cards, groups):
    valid = []
    for group in groups:
        found = [False]*len(cards)
        for card in cards:
            for part in group:
                if card in part:
                    found[cards.index(card)]=True
        if not False in found:
            valid.append(group)
    return valid

'''
This function checks if the raise that the player wants to make is valid.
This is basically done in 4 parts:
1. get all the possible combinations of the selected cards to raise, that the player is able to raise with the raiseCard (e.g. if raiseCard
    is of value 10, and player tries to raise a5 b5 c5 d5 10, the combinations would be
    (a5 b5),(b5 c5),...,(10)
2. make combinations of groups that already have the right points and then chop down the possibilities so, that only groups that have as much cards as the player has chosen cards e.g.
    -->(a5 b5)(c5 d5)(10),...,(a5 b5)(a5 c5)(10)
3. accept only groups, where cards appear only once, e.g.
    (a5 b5)(c5 d5)(10),...,(a5 b5)(a5 c5)(10) ---> (a5 b5)(c5 d5)(10)
4. if there are groups that obey all the criterias above, the raise is valid and the function returns True
'''
def validRaise(raiseCard, cards):
    value = raiseCard.getHandValue()
    valid = getValidGroups1(value,cards)
    valid =  getValidGroups2(len(cards),valid)
    valid = getValidGroups3(cards, valid)
    return len(valid)!=0


'''
This function calculates points after a round.
Parameters: players, cardPoints(normally 0, if no one got points for the most cards on the last round, this value is raised by one),
spadesPoints (same as cardPoints but for spades-cards)
'''
def calculatePoints(players,cardPoints,spadesPoints):
    
    '''
    cottages and aces, special cards
    '''
    txt='\n'
    for player in players:
        points=player.getCottages()
        player.updatePoints(points)
        player.clearCottages()
        if points >0:
            txt1= player.getName()+" got "+str(points)+" points from cottages.\n"
            txt+=txt1
        
        points=player.getStack().getSureValue()
        if points>0:
            txt1= player.getName()+" got "+str(points)+" points from aces/special cards.\n"
            txt+=txt1
        player.updatePoints(points)
    
    
    '''
    most cards and most spades
    '''
    cardAmount=0
    spadesAmount=0
    pl1=[]
    pl2=[]
    for player in players:
        
        if player.getStack().getAmountOfCards()==cardAmount:
            pl1.append(player)  
        if player.getStack().getAmountOfCards()>cardAmount:
            cardAmount=player.getStack().getAmountOfCards()
            pl1=[]
            pl1.append(player)
            
        if player.getStack().getAmountOfSuit(Card.SPADES)==spadesAmount:
            pl2.append(player)  
        if player.getStack().getAmountOfSuit(Card.SPADES)>spadesAmount:
            spadesAmount=player.getStack().getAmountOfSuit(Card.SPADES)
            pl2=[]
            pl2.append(player)
        
            
    if len(pl1)==1:
        txt1= pl1[0].getName()+" got "+str(cardPoints+1)+" points from most cards.\n"
        txt+=txt1
        pl1[0].updatePoints(cardPoints+1)
        cardAmount=0
    else:
        cardAmount=cardPoints
        cardAmount+=1
        
    if len(pl2)==1:
        txt1= pl2[0].getName()+" got "+str(spadesPoints+1)+" from most spades.\n"
        txt+=txt1
        pl2[0].updatePoints(spadesPoints+1)
        spadesAmount=0
    else:
        spadesAmount=spadesPoints
        spadesAmount+=1
        
    return cardAmount, spadesAmount,txt
        
        
def putCardToBoard(card,game,player):
    if card not in player.getHand().getCards():
        print "ERROR, this should never happen."
    player.getHand().removeCard(card)
    game.getBoard().addCard(card)
     
     
def dealToPlayers(game):
    for i in game.getPlayers():
        cards = game.deal(4)
        i.addCardsToHand(cards)
        
'''
deletes cards from board and moves them to players stack
'''
def moveCardsToStack(raiseCard,cards,game,player):
    game.getBoard().removeCards(cards)
    player.getHand().removeCard(raiseCard)
    player.addCardsToStack(cards)
    player.addCardToStack(raiseCard)    
    
    
    
    
    
  