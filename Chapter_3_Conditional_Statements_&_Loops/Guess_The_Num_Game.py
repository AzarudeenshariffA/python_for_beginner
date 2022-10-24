import random
guess_num=(random.randint(1, 100))
game_over = 0
steps=0
while(game_over!=1):
    user_num = int(input("Enter a number between 1 to 100: "))
    if(steps<10):
        if(user_num==guess_num):
            print(f"You Won The Game in {steps+1} Step")
            game_over=game_over+1
        elif(user_num>guess_num):
            print("The numbe is too high")
            steps+=1
        else:
            print("the number is too low")
            steps+=1
    else:
        print("Sorry Number Of Trials Exit... Try Again Later...")