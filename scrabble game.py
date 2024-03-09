#File:CS112_A1_T2_20230467
"""Number scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw."""
#Author: Yassine said hassan Mahmoud
#ID: 20230467
def check_win(player_moves):                     #first I made a function that check the winner
    winning_combinations = [[9, 6], [9, 4, 2], [8, 7], [8, 4, 3], [8, 5, 2], [9, 5, 1], [7, 5, 3], [7, 6, 2],[4,5,6],[1, 5, 9],[2, 5, 8],[3, 5, 7],[3, 6, 6],[1, 6, 8],[2, 4, 9]] # this is al the combos that makes any player win
    for combo in winning_combinations:                                   #then we made a loop to see which player has got any combos from them
        if all(num in player_moves for num in combo):                    # to do it we used the built-in function all which check if any combo from the list in code no.9 exist in the players choice or not
            return True                                                  # if it exists it will return true
    return False                                                         # if it is not it will return false
################################################ the game ################################################################
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]                # the list of the game numbers
list_of_p1 = []                                              # player one choices
list_of_p2 = []                                              # player two choices

while list_of_numbers:
    while True :
        try:
            p1_move = int(input(f"player one, please pick a number from the list {list_of_numbers}: "))
            while p1_move not in list_of_numbers:# the first player input and I show him the numbers that he should to choose by putting the list in a curly bracket using f-string
                p1_move = int(input(f"please pick a valid number{list_of_numbers}: "))
            break
        except ValueError:
            print('invalid input')


           # checking the valid choice
    print(f"Player one has chosen {p1_move}.")       # if it is valid the second player will know the first one's choice
    list_of_p1.append(p1_move)                       # and then the number will be removed from the list and will add to first player choices
    print(f"player one has {list_of_p1}")
    list_of_numbers.remove(p1_move)

    if check_win(list_of_p1):                               # then we will chcck if the player has collected at least three numbers will make him reach 15 or not and if he reached it he will win and the game end
        print("Player1 won")
        break

    if not list_of_numbers:
        break
    while True:
        try:
            p2_move = int(input(f"player two, please pick a number from the list {list_of_numbers}: "))
            while p2_move not in list_of_numbers:
                p2_move = int(input(f"please pick a valid number from {list_of_numbers}: "))
            break
        except ValueError:
            print('invalid input')

    print(f"Player two has chosen {p2_move}.")
    list_of_p2.append(p2_move)
    print(f"player two has {list_of_p2}")
    list_of_numbers.remove(p2_move)

    if check_win(list_of_p2):
        print("Player2 won")
        break
if not list_of_numbers and not check_win(list_of_p1) and not check_win(list_of_p2):  # checking the draw if anyone from the two players didn't win that means the function will return false
    print(" draw ")