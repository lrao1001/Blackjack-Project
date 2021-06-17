import tkinter
import random
import tkinter.font as tkFont


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
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='sunken').pack(side='left')
    return next_card


# Functions for dealing cards to both dealer & player
def deal_player():
    global player_score
    global player_ace

    card_value = deal_cards(player_card_frame)[0]
    if card_value == 1 and not player_ace:
        card_value = 11
    player_score += card_value
    if player_score > 21 and player_ace:
        player_score -= 10
        player_ace = False
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("DEALER WINS")

def deal_dealer():
    deal_cards(player_card_frame)


# Set up screen for dealer & player
mainWindow = tkinter.Tk()
mainWindow.title("BLACKJACK")
mainWindow.geometry('640x480')
mainWindow.configure(bg='#009933')

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text, font=fontStyle)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='raised', borderwidth=1, bg='#009933')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", bg='#009933', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, bg='#009933', fg='white').grid(row=1, column=0)

player_score = 0
player_ace = False

    # embed frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, bg='#009933')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", bg='#009933', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, bg='#009933', fg='white').grid(row=3, column=0)


player_card_frame = tkinter.Frame(card_frame, bg='#009933')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # Buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="DEALER", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="PLAYER", command=deal_player)
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


