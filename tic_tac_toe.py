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
    #check for win
    if board[1] + board[5] + board[9] == "xxx" or board[1] + board[14] + board[27] == "xxx" or board[1] + board[18] + board[35] == "xxx" or board[5] + board[14] + board[31] == "xxx" or board[9] + board[18] + board[27] == "xxx" or board[9] + board[22] + board[35] == "xxx" or board[14] + board[18] + board[22] == "xxx" or board[27] + board[31] + board[35] == "xxx":
        print(board)
        print("Player x wins!")
        game_over = True
        break
    if board[1] + board[5] + board[9] == "ooo" or board[1] + board[14] + board[27] == "ooo" or board[1] + board[18] + board[35] == "ooo" or board[5] + board[14] + board[31] == "ooo" or board[9] + board[18] + board[27] == "ooo" or board[9] + board[22] + board[35] == "ooo" or board[14] + board[18] + board[22] == "ooo" or board[27] + board[31] + board[35] == "ooo":
        print(board)
        print("Player o wins!")
        game_over = True
        break

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