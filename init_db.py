import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cardD = {1: ['Diamonds', 'A', 'link'], 2: ['Diamonds', '2', 'link'], 3: ['Diamonds', '3', 'link'], 
4: ['Diamonds', '4', 'link'], 5: ['Diamonds', '5', 'link'], 6: ['Diamonds', '6', 'link'], 7: ['Diamonds', '7', 'link'], 
8: ['Diamonds', '8', 'link'],9: ['Diamonds', '9', 'link'], 10: ['Diamonds', '10', 'link'], 11: ['Diamonds', 'Jack', 'link'],
12: ['Diamonds', 'Queen', 'link'], 13: ['Diamonds', 'King', 'link'], 
14:['Spades', 'A', 'link'],15: ['Spades', '2', 'link'],16: ['Spades', '3', 'link'],17: ['Spades', '4', 'link'],
18:['Spades', '5', 'link'], 19: ['Spades', '6', 'link'],20: ['Spades', '7', 'link'],21: ['Spades', '8', 'link'],
22: ['Spades', '9', 'link'],23: ['Spades', '10', 'link'],24:['Spades', 'Jack', 'link'],25: ['Spades', 'Queen', 'link'], 
26: ['Spades', 'King', 'link'],
27: ['Hearts', 'A', 'link'],28:['Hearts', '2', 'link'],29: ['Hearts', '3', 'link'],30: ['Hearts', '4', 'link'],
31:['Hearts', '5', 'link'],32:['Hearts', '6', 'link'],33:['Hearts', '7', 'link'],34:['Hearts', '8', 'link'],
35:['Hearts', '9', 'link'],36:['Hearts', '10', 'link'],37:['Hearts', 'Jack', 'link'],38:['Hearts', 'Queen', 'link'], 39:['Hearts', 'King', 'link'],
40:['Clubs', 'A', 'link'],41:['Clubs', '2', 'link'],42:['Clubs', '3', 'link'],43:['Clubs', '4', 'link'],
44:['Clubs', '5', 'link'],45:['Clubs', '6', 'link'],46:['Clubs', '7', 'link'],47:['Clubs', '8', 'link'],
48:['Clubs', '9', 'link'],49:['Clubs', '10', 'link'],50:['Clubs', 'Jack', 'link'],51:['Clubs', 'Queen', 'link'],
52:['Clubs', 'King', 'link']}

for i in range(52):
    cur.execute("INSERT INTO cards (title, suit, content) VALUES (?, ?, ?)",
                ( cardD[i+1][1], cardD[i+1][0], cardD[i+1][2])
                )

connection.commit()
connection.close()