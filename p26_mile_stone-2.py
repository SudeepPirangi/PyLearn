"""
Milestone project 2
Question - https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/08-Milestone%20Project%20-%202
"""

# Programmer's comment - This game play is incomplete, I'll comeback to this later

from random import shuffle

COMPUTER = "Computer"

class Deck:
    """Create a deck of 52 cards"""
    suits = ["♦️", "❤️", "♠️", "♣️" ]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append(number + suit)

    def __str__(self):
        return " ".join(self.deck)

    def deal(self):
        """Take out a card from deck"""
        return self.deck.pop()

class Player():
    """Creates a Player for the game"""
    def __init__(self, name, chips = 1000):
        self.name = name
        self.cards = []
        self.bet = 0
        self.chips = chips
        self.count = 0
        self.aces = 0

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards and {self.bet} bet"

    def show_cards(self):
        """Displays all the cards of the player"""
        print(f"\n{self.name} Cards - [{self.count}]")
        print(" ".join(self.cards))

    def add_card(self, card):
        """Add a card to players hand"""
        value = card[:-1]
        if value == 'A':
            self.aces += 1
            self.count += 11
        elif value == 'J' or value == 'Q' or value == 'K':
            self.count += 10
        else:
            self.count += int(value)
        self.cards.append(card)

def ask_chips(player):
    """Ask real player for the total chips they hold"""
    chips = 0
    got_chips = False
    while not got_chips:
        try:
            chips = int(input(f"\n{player.name}, how many chips have you got --> "))
            player.chips = chips
            got_chips = True
        except ValueError:
            print("Nah, you have to enter a number")

def ask_bet(player):
    """Ask real player for a bet"""
    bet = 0
    got_bet = False
    while not got_bet:
        try:
            bet = int(input(f"\n{player.name}, place some bet --> "))
            if bet > player.chips:
                print("You cannot bet more than the chips you hold")
            elif bet <= 0:
                print("Now if you are done with your misery, let's continue")
            else:
                player.bet = bet
                got_bet = True
        except ValueError:
            print("Nah, you have to enter a number")

def is_player_busted(player, opponent):
    """Checks if the player is busted"""
    if player.count > 21:
        return True
        

def hit_or_stand(player, opponent, deck):
    """Allows the player to choose between Hit or Stand"""
    while True:
        decision = input(f"\n{player.name}, you wish to HIT or STAND? Choose H or S --> ")
        decision = decision.lower()

        if decision != 'h' or decision != 's':
            print("You don't obey me! I kick you out")
            return 'X'
        elif decision == 'h':
            player.add_card(deck.deal())
            player.show_cards()
        elif decision == 's':
            print(f"{player.name} stands at {player.count}")

        
        if is_player_busted(player, opponent):
            print(f"{player.name}, you are BUSTED. {opponent.name}, you WIN")
            return False

def play():
    """Game play"""
    while True:
        try:
            deck = Deck()
            print(deck.deck)

            shuffle(deck.deck)
            print("\nShuffled Deck", deck.deck)

            human = Player("Human")
            computer = Player(COMPUTER)

            ask_chips(human)
            ask_bet(human)

            print(human)
            print(computer)

            computer.add_card(deck.deal())
            computer.add_card(deck.deal())
            human.add_card(deck.deal())
            human.add_card(deck.deal())

            print(f"\n{computer.name} cards -> {computer.cards[0]}, X")
            print(f"{human.name} cards -> {" ,".join(human.cards)}")

            print("\nHuman's turn")
            result = hit_or_stand(human, computer, deck)
            if result == 'X':
                print('You are being Kicked-out')
            elif not result:
                human.chips -= human.bet
                return

            result = hit_or_stand(computer, human, deck)
            if result == 'X':
                print('You are being Kicked-out')
            elif not result:
                human.chips -= human.bet
                return

        except:
            print("some error")
            return

print("Game Over!!!")
