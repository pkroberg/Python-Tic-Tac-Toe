board = "[ ] [ ] [ ] \n[ ] [ ] [ ] \n[ ] [ ] [ ]"

position_to_insert = 1
character_to_insert = "x"
new_board = board[:position_to_insert] + character_to_insert + board[position_to_insert + 1:]

print(new_board)