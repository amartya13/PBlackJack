import random
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten,', 'jack', 'queen', 'king', 'ace')
values =  {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

playing = True

class Card(self, suit, rank):
	def __init__():
		self.suit = suit
		self.rank = rank
	
	def __str__():
		return self.rank + ' of ' + self.suit

class Deck:
		def __init__(self):
			self.deck = []
			for suit in suits:
				for rank in ranks:
					self.deck.append(Card(suit, rank))
	
	def __str__(self):
	deck_comp = ''
		for card in self.deck:
			deck_comp += '\n '+card.__str__()
			return 'The deck has:' + deck_comp
	
	def shuffle(self):
		random.shuffle(self.deck)
	
	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0
    
	
	def addcard(self, card):
		self.value += values[card, rank]
		if card.rank == 'Ace':
			self.aces += 1
	
	def adjust_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips:
	def __init__(self):
		self.total = 100
		self.bet = 0
	
	def win_bet(self):
		self.total += self.be
	
	def loose_bet(self):
		self.total -= self.bet

def take_bet:
	while True:
		try:
			chips.bet = int(input('How many chips would you like to bet? '))
			except ValueError:
			print('Sorry, a bet must be an integer!')
		else:
			if chips.bet > chips.total:
				print("Sorry, your bet can't exceed",chips.total)
			else:
				break

def hit(deck, hand)
		hand.add_card(deck.deal())
		hand.adjust_for_ace()

def hit_or_stand(deck, hand):
	global playing

	while True:
		x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player stands. Dealer is playing.")
			playing = False

		else:
			print("Sorry, please try again.")
			continue
	break playing
    
    

def show_some(player, dealer):
	print("\nDealer's Hand:")
	print(" <card hidden>")
	print('',dealer.cards[1])  
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player, dealer): 
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)

def player_busts():
	print("Player busts!")
	chips.lose_bet()

def player_wins():
	print("Player wins!")
	chips.win_bet()

def dealer_busts():
	print("Dealer busts!")
	chips.win_bet()
    
def dealer_wins():
	print("Dealer wins!")
	chips.lose_bet()
    
def push():
	print("Dealer and Player tie! It's a push.")



print('Welcome to BlackJack! Get as close to 21 as you can exeeding the limit!\n\
Dealer hits until she reaches 17. Aces count as 1 or 11.')

deck = Deck()
deck.shuffle()
    
player_hand = Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())
    
dealer_hand = Hand()
dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())
            
player_chips = Chips() 
    
take_bet(player_chips)
    
show_some(player_hand,dealer_hand)

    if player_hand.value <= 21:
        
		while dealer_hand.value < 17:
			hit(deck,dealer_hand)    
    
		show_all(player_hand,dealer_hand)
        
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		else:
			push(player_hand,dealer_hand)        
     
	print("\nPlayer's winnings stand at",player_chips.total)
    
	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
	if new_game[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thanks for playing!")
		break