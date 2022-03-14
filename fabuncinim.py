# Fibonacci Nim #8
# student name:ahmed yasser bastawessy
# id:20210048
import random
coins = random.randint(10,50) # giving a random number for coins, Maximum 50 so that the game doesn't take long
print("the number of coins is", coins)
while (coins != 0):
    print("Player1 turn")
    player1 = int(input())
    while (player1 == coins):
        print("play again")
        player1 = int(input())
    while (player1 > coins):
        print("play again")
        player1 = int(input())
    while (player1 < 0):
        print("play again")
        player1 = int(input())
    coins = coins - player1
    while (coins != 0):
        print("the number of coins is", coins)
        print("Player2 turn, you can pick up to ", (player1*2))
        player2 = int(input())
        while (player2 > coins):
            print("play again")
            player2 = int(input())
        while (player2 > (2 * player1)) or (player2 < 0):
            print("enter a valid number")
            player2 = int(input())
        while (player2 <= coins):
            print("Player2 wins")
            exit()
        coins = coins - player2
        print("the number of coins is", coins)
        print("Player1 turn, you can pick up to ", (player2*2))
        player1 = int(input())
        if (player1 <= coins):
            print("Player1 wins")
            exit()

        while (player1 > 2 * player2) or (player1 < 0):
            print("enter a valid number")
            player1 = int(input())
        while (player1 > coins):
            print("play again")
            player1 = int(input())
        coins = coins - player1
