'''Blackjack
    Card - rank & suit (image)
    Hand - collection of cards (hit score)
    Deck - collection of cards (shuffle dead)
'''

RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = ['A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10]
class Hand:
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    def add_card(self, card):
        pass
    
    def get_value(self):
        pass
        
    def busted(self):
        pass
        
    def draw(self, canvas, p):
        pass
      
        
# define deck class
class Deck:
    def __init__(self):
        pass
        
    def shuffle(self):
        pass
        
    def deal_card(self):
        pass
        
