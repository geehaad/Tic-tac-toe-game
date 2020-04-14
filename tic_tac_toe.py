import itertools

    
def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] !=0:
           return True
        else:
           return False

    #Horizontal Winner
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner HORIZONTALLY!!!")
            return True
    
    #Vertical Winner
    for col in range(len(game)):
        check =[]
        for row in game:
            # print(colm[0])
            check.append(row[col])
        if all_same(check) !=0:
            print(f"Player {check[0]} is the winner VERTICALLY!!!")
            return True

    #Diagonal Winner
    diagsX = []
    for col,row in enumerate(reversed(range(len(game)))):
        print(col,row)
        diagsX.append(game[row][col])
    if all_same(diagsX):
        print(f"Player {diagsX[0]} is the winner DIAGONALLY(/)!!!")
        return True

    diagsY = []
    for ix in range(len(game)):
        diagsY.append(game[ix][ix])
    if all_same(diagsY):
        print(f"Player {diagsY[0]} is the winner DIAGONALLY!!!(\\)")
        return True

    return False

def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] !=0:
           print("This Position is ACCUPADO! Choose Another!")
           return game_map,False
        print("  "+" ".join(str(i) for i in range(len(game_map) )))
        if not just_display:
            game_map[row][column]=player
        for count, row in enumerate(game):
            print(count,row)
        return game_map, True
    except IndexError as e:
        print("Somthing went wrong!!",e)
        return game_map,False

play = True
players = [1, 2]
while play:
    game_size = int(input("What size of game you want? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won= False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)

        print(f"Current Player: {current_player}")
        played =False

        while not played:
            column_choice = int(input("what column do you want to play? (0, 1, 2): "))
            row_choice = int(input("what row do you want to play? (0, 1, 2): "))
            game, played = game_board(game,current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Byeeeeee")
                play = False
            else:
                print("Not A Valid Answer, so... C U l8r aligator")
                play = False


    
