# firedice
currently developed to just about round 2 functionality

Basic attempt to build a workflow dynamics simulator game.  The original game consists of:
-5 colored sheets of paper, to represent the work queues (e.g. Design, Develop, Test, UAT, Done)
-10+ white dice
-5+ red dice
-deck of playing cards
-whiteboard marker

Gameplay (round 1):
-8 days of play, 4 dice (to start) are rolled individually per "day".
-you must declare which queue you are rolling on, to bring cards into prior to rolling
-there must be cards available in the prior queue in order to bring them in (the Deck itself would be queue Zero)
-at the end of each "day", cards that are "done" are valued at:
--->J/Q/K/A (16 cards) = 11 pts
--->2-9 (36 cards) = face value
--->Jokers (2 cards) = 20 points

Gameplay (round 2):
-same as above, plus...
--->at the end of each "day", cards that are not "done" get a tick mark counter for WIP (work in progress)
--->at the end of each "day", card values are the same as above, BUT WIP counts are subtracted from the card value when completed
-------> (e.g. a K with 3 WIP counts: 11 - 3 = 8 points)
--->at the end of the game, cards that are not "done" have the same values as above, but the WIP is ADDED to the card value, and the overall total is subtracted from the "done" value (e.g. 137 points delivered, with a Queen left in Q4, with 4 WIP counts (-15 pts) will result in an overall score of 122 points)

Gameplay (round 3):
-same as above, plus...
--->wasted work is tracked (e.g. you have 4 cards in the 1st queue, and you are rolling for queue 2.  You roll a 6.  This creates 2 points of wasted work)
--->overall score is DELIVERED POINTS - INCOMPLETE POINTS - (WASTED WORK POINTS x 5)

Gameplay (round 4):
-same as above, plus...
--->ability to "spend 25 points" to get an additional white die
--->ability to trade in 2 white dice to get a red (fire) die
------> a red die can pick any queue AFTER it has been rolled
