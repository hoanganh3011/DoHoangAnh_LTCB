import random
money=100
total_games=win_games=lose_games=0
while True:
    if money<5:
        print("You don't have enough money to play")
        break
    money-=5
    print('Computer thinks a number from 1 to 100')
    comp_number = random.randint(1, 100)
    level = int(input('choose level [1,2,3]? '))
    # 1: easy, 2: medium; 3: hard
    times = 10 if level == 1 else 5 if level == 2 else 3
    is_win = False
    for time in range(times):
        your_num = int(input("Enter your guessing number #" + str(time + 1) + ": "))
        if your_num == comp_number:
            is_win = True
            break
        else:
            if your_num < comp_number:
                print('too low!')
            else:
                print('too high')
        if is_win and time + 1 >= times:
           print("You are Genius!!!!.")
           win_games += 1
        if time + 1 >= times:
           print('----------------')
    print('Game over!')
    lose_games += 1

    print('----------------')
    cont = input('Dare to you to play [y/n]: ')
    if cont == 'n' or cont == 'N':
        break
print(f"You won {win_games} games out of {lose_games} games, Your money is {money}")