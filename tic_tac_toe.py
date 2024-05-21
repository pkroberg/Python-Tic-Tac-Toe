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
    'bottomright': 35,
}
#turn counter
turn = 1

#game loop
while not game_over:
    #player 1 character selection
    if player_1_character == "":
        player_1_character = input("Player 1, would you like to be 'x' or 'o'?").lower()
        player_2_character = "o" if player_1_character == "x" else "x"
    
    #display current game board
    print(board)

    #get player input
    if turn % 2 == 0:
        action = input("Player 2, where would you like to go?").lower()
        turn += 1
    else:
        action = input("Player 1, where would you like to go?").lower()
        turn += 1

    #validate input position
    if action not in positions:
        print('Invalid input. Please enter, "topleft, top, topright, left, middle, right, bottomleft, bottom, bottomright')
        continue

    #retrieve position to insert character
    position_to_insert = positions[action]

    #update board
    if turn % 2 == 0:
        board = board[:position_to_insert] + player_1_character + board[position_to_insert + 1:]
    else:
        board = board[:position_to_insert] + player_2_character + board[position_to_insert + 1:]
    
print("Game Over")