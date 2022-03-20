from random import randint

outcome = ['odd', 'even']
marbles_user = 10 
marbles_comp = 10 
l = True

def endgame():
    if marbles_comp <= 0:
        print ("You won")
        l = False
        exit()
    if marbles_user <= 0:
        print ("You lost")
        l = False
        exit()

while l:
    print ('Odd or even ? (1 for odd, 2 for even)')
    comp = randint(1, 2)
    user = int(input())

    print ('Wager your marbles, you have', marbles_user)
    wager = int(input())
    #correct
    if user == comp:
        print ("correct")
        marbles_user += wager
        marbles_comp -= wager
        print ('You now have', marbles_user, 'marbles')
        endgame()
    #incorrect
    elif user != comp:
        print ("incorrect")
        marbles_user -= wager
        marbles_comp += wager
        print ('You now have', marbles_user, 'marbles')
        endgame()


    
    print ("AI's turn")
    print ("Odd or even ? (1 for odd, 2 for even)")
    player_choice = int(input())
    comp_guess = randint(1, 2)
    comp_wager = randint(1, marbles_comp)

    #correct
    if comp_guess == player_choice:
        print('Ai chose', outcome[comp_guess - 1], 'correctly')
        marbles_user -= comp_wager
        marbles_comp += comp_wager
        print ("AI's wager is", comp_wager)
        print ('You now have', marbles_user, 'marbles')
        endgame
        
    #incorrect
    elif comp_guess != player_choice:
        print('Ai chose', outcome[comp_guess - 1], 'incorrectly')
        marbles_user += comp_wager
        marbles_comp -= comp_wager
        print ("AI's wager is", comp_wager)
        print ('You now have', marbles_user, 'marbles')
        endgame()
        
    else:
        print ("Unexpexted error has happened")
    endgame()


    