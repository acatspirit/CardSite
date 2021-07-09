from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort



def get_db_connection():
    """Makes a connection with the card database for a desired card"""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_card(card_id):
    """gets the card of the specified id from the database"""
    conn = get_db_connection()
    card = conn.execute('SELECT * FROM cards WHERE id = ?',
                        (card_id,)).fetchone()
    conn.close()
    if card is None:
        abort(404)
    return card

def get_suit(card_suit):
    """gets the suit of a card from the card id specified"""
    conn = get_db_connection()
    suit = conn.execute('SELECT * FROM cards WHERE suit = ?',
                        (card_suit,)).fetchone()
    conn.close()
    if suit is None:
        abort(404)

    return suit

app = Flask(__name__)


#maybe the problem is that I'm not referencing suit as an attribute of a card object

@app.route('/')
def index():
    #get all the cards
    conn = get_db_connection()
    cards = conn.execute('SELECT * FROM cards').fetchall()
    conn.close()

    #make lists to that only 1 card per suit is displayed
    suits = []
    cardL = []
    for card in cards:
        suit = card[2]
        if suit not in suits:
            suits += [suit]
            cardL += [card]
    return render_template('index.html', suits = suits, cardL = cardL)



@app.route('/cardSelect/<suit>')
def cardSelect(suit = 'Diamonds'):
    """get all the cards from the database and put them on the index page"""
    print(suit)
    conn = get_db_connection()
    cards = conn.execute('SELECT * FROM cards').fetchall()
    conn.close()
    
    cardL = []
    for card in cards:
        card_suit = card[2]
        if card_suit == suit:
            cardL += [card]



        
    return render_template('cardSelect.html', cards = cardL)


@app.route('/cardSelect/<suit>/<int:card_id>')
def card(card_id, suit):
    """get the card ID and display the card"""
    card = get_card(card_id)
    return render_template('card.html', card=card)