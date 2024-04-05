#initial game start
board = "[ ] [ ] [ ] \n[ ] [ ] [ ] \n[ ] [ ] [ ]"
game_over = False
player_1_character = ""
player_2_character = ""

positions = {
    'topleft': 1,
    'top': 5,
    'topright': 9,
    'left': 14,
    'middle': 18,
    'right': 22,
    'bottomleft': 27,
    'bottom': 31,
   ' bottomright': 35,
}

#game loop
while not game_over:
    #display current game board
    print(board)

    #get player input
    action = input("Where would you like to go?").lower()

    #validate input position
    if action not in positions:
        print('Invalid input. Please enter, "topleft, top, topright, left, middle, right, bottomleft, bottom, bottomright')
        continue

    #retrieve position to insert character
    position_to_insert = positions[action]

    #update board
    board = board[:position_to_insert] + "x" + board[position_to_insert + 1:]
    
print("Game Over")