import random
import itertools

def builddeck():
    global DECK  # make this avaiable everywhere
    SUITS = 'shdc'  # suits of the cards (not absolutely necessary...but helps to build the deck)
    RANKS = '23456789TJQKA'  # card ranks
    DECK = list('_'.join(card) for card in itertools.product(RANKS, SUITS))  # build core card deck
    DECK = DECK + ["J_1", "J_2"]

def buildQs():
    global Q1
    global Q2
    global Q3
    global Q4
    global Q5
    Q1 = []
    Q2 = []
    Q3 = []
    Q4 = []
    Q5 = []

def roll():
    x = random.randint(1, 6)
    return (x)

def flip():
    if len(DECK) == 0:
        return "[XXX]"
    y = DECK.pop(random.randint(0, len(DECK) - 1))  # random card draw and removal (pop) from deck
    return y

def status():
    print("\nStatus by Q: CARD + (WIP Count)]")
    count = 0
    suit = ""
    for q in (Q1, Q2, Q3, Q4, Q5):
        print("\nQ" + str(count + 1) + ":", len(q), "Cards\n============")
        for each in q:
            if each[0][2] is "s":
                suit = " \U00002660"  # spade - last num 4, 0  (outline vs solid)
            elif each[0][2] is "h":
                suit = " \U00002663"  # heart  - last num 1, 3  (outline vs solid)
            elif each [0][2] is "d":
                suit = " \U00002666"  # diamond - last num 2, 6 (outline vs solid)
            elif each [0][2] is "c":
                suit = " \U00002665"  # club  - last num 7, 5  (outline vs solid)
            else:
                suit = "oker"  # essentially creates the word "Joker" since there is no suit
            print(each[0][0]+suit, "(" + str(each[1]) + ")")
        count += 1

def shortstat():
    count = 0
    for q in (Q1, Q2, Q3, Q4, Q5):
        print("Q" + str(count + 1) + ":", "* " * len(q))
        count += 1

def wipit():
    for q in (Q1, Q2, Q3, Q4):
        for each in q:
            each[1] += 1

def scoredone():  # TODO rebuild scoring for on the fly as well as final
    score = 0
    global Q5
    for each in Q5:
        if each[0][0] in ("Q", "K", "A"):
            each[2] = 11 - each[1]
        elif each[0][0] in ("T"):
            each[2] = 10 - each[1]
        elif each[0][0] in ("J"):
            if each[0][2] in ("1", "2"):
                each[2] = 20 - each[1]
            else:
                each[2] = 11 - each[1]
        else:
            each[2] = int(each[0][0]) - each[1]
        score += each[2]
    return (score)

def wiploss():
    score = 0
    global Q1
    global Q2
    global Q3
    global Q4
    for q in (Q1, Q2, Q3, Q4):
        for each in q:
            if each[0][0] in ("Q", "K", "A"):
                each[2] = 11 + each[1]
            elif each[0][0] in ("T"):
                each[2] = 10 + each[1]
            elif each[0][0] in ("J"):
                if each[0][2] in ("1", "2"):
                    each[2] = 20 + each[1]
                else:
                    each[2] = 11 + each[1]
            else:
                each[2] = int(each[0][0]) + each[1]
            score += each[2]
    return (score)

builddeck()
buildQs()

d = 1
days = 8
loss = 0

def day():
    global loss
    global Q1
    global Q2
    global Q3
    global Q4
    global Q5
    rolls = 4
    while rolls > 0:
        print("\nDay", (days - 9) * -1, "-", "You have", rolls, "rolls remaining.")
        shortstat()
        while True:
            try:
                q = int(input("What Q would you like this roll advance cards into? (1-5): "))
                break
            except:
                print("Try Again - valid response is 1, 2, 3, 4, or 5)")
                continue
        die = roll()
        rolls -= 1
        print("\nYou rolled a", str(die) + ".")  # , " Here are your cards:")
        for each in range(die):
            if q == 1:      # TODO move this function to flip; only Q1 instaciates a card
                card = flip()
                new = [[card, 0, 0, 0]]  # card, WIP count, value if delivered, value if not delivered (need to do the last part)
                Q1 = Q1 + new
            if q == 2:  # TODO refactor to be a bit cleaner
                try:
                    card = Q1.pop(random.randint(0, len(Q1) - 1))
                    Q2 = Q2 + [card]
                    # print (each+1, ":", card[0])
                except:
                    print("Move", each + 1, ": Loss of effort; no card available")
                    loss += 1
            if q == 3:
                try:
                    card = Q2.pop(random.randint(0, len(Q2) - 1))
                    Q3 = Q3 + [card]
                    # print (each+1, ":", card[0])
                except:
                    print(each + 1, ": Loss of effort; no card available")
                    loss += 1
            if q == 4:
                try:
                    card = Q3.pop(random.randint(0, len(Q3) - 1))
                    Q4 = Q4 + [card]
                    # print (each+1, ":", card[0])
                except:
                    print(each + 1, ": Loss of effort; no card available")
                    loss += 1
            if q == 5:
                try:
                    card = Q4.pop(random.randint(0, len(Q4) - 1))
                    Q5 = Q5 + [card]
                    # print (each+1, ":", card[0])
                except:
                    print(each + 1, ": Loss of effort; no card available")
                    loss += 1
    print("\nDay", (days - 9) * -1, "complete.  Here is the day closing summary:")
    shortstat()

print("\n               WELCOME TO FIRE DICE!")
print("=========================================================")
print("| 4 die rolls per day, 8 days of play.  GET STUFF DONE! |")
print("| > Scoring for completed work:  face value - WIP count |")
print("| > Scoring for incomplete work: face value + WIP count |")
print("| > 2,3,4,5,6,7,8,9,T = #    J,Q,K,A = 11    Joker = 20 |")
print("---------------------------------------------------------")

while days != 0:
    print("\n**", days, "days remaining **")
    z = input("(R)oll, (B)oard Stats, e(X)it: ")
    if z in ["r", "R"]:
        day()
        days -= 1
        wipit()  # comment this out if you don't want to score against WIP
        wiploss()
    if z in ["b", "B"]:
        status()
    if z in ["x", "X"]:
        quit()
if days == 0:
    status()  #TODO this will become a FINAL status
    print("\n***********************************")
    print("Total Delivery:", scoredone(), "pts of value")
    print("Total lost effort:", loss, "moves")
    print("Total WIP loss:", wiploss(), "pts of effort and lost value")
