#importing modules
import itertools, random
#make a deck of cards
deck = list(itertools.product(range(1,14),['Spade', 'Heart, Diamond', 'Club']))

#Shuffle the cards

random.shuffle(deck)

#Draw the cards

print ('you got: ')
for i in range(5):
    print(deck[i cZD z][0], 'of', deck[i][1])


