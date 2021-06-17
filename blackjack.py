import tkinter
import random

mainWindow = tkinter.Tk()


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    EXTENSION = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = "Cards/{}_{}.{}".format(str(card), suit, EXTENSION)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        for card in face_cards:
            name = "Cards/{}_{}.{}".format(str(card), suit, EXTENSION)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_cards(frame):
    next_card = deck.pop()
    tkinter.Label(frame, image=next_card[1], relief='sunken').pack(side='left')
    return next_card


# Functions for dealing cards to both dealer & player
def deal_dealer():
    deal_cards(dealer_card_frame)


def deal_player():
    deal_cards(player_card_frame)


# Set up screen for dealer & player
mainWindow.title("BLACKJACK")
mainWindow.geometry('640x480')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, bg='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", bg='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, text=dealer_score_label, bg='green', fg='white').grid(row=1, column=0)

    # embed frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, bg='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", bg='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, text=player_score_label, bg='green', fg='white').grid(row=3, column=0)


player_card_frame = tkinter.Frame(card_frame, bg='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # Buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="DEALER")
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="PLAYER")
player_button.grid(row=0, column=1)

# Load cards
cards = []
load_images(cards)
print(cards)

# Create a new deck of cards & shuffle them
deck = list(cards)
random.shuffle(deck)

# Create the list storing player's and dealer's hands
dealer_hand = []
player_hand = []


mainWindow.mainloop()