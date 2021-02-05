import random

count = 0
winnings = 0

while True:
    count += 1
    print("\n")


    def intersection(num_list, ball_list):
        temp = set(ball_list)
        same_list = [value for value in num_list if value in temp]
        matches = len(same_list)
        return matches


    # User input
    num_list = random.sample(range(1, 55), 6)
    bonus_ball = random.randint(1, 10)
    print(f'Player Numbers: {num_list} with bonus ball: {bonus_ball}')

    # Generate random set of numbers from ball machine & print results
    ball_list = random.sample(range(1, 55), 6)
    ball_bonus_ball = random.randint(1, 10)
    print(f'Ball Machine Numbers: {ball_list} with bonus ball: {ball_bonus_ball}')

    # Printing matched numbers
    print(f'Player matched {intersection(num_list, ball_list)} numbers')

    # calculating winnings
    if intersection(num_list, ball_list) == 0:
        print(f'Player won £0 from: {count} tickets for a total of: £{winnings}')

    elif intersection(num_list, ball_list) == 1:
        print(f'Player won £0 from: {count} tickets for a total of: £{winnings}')

    elif intersection(num_list, ball_list) == 2:
        winnings += 2
        print(f'Player won £2 from: {count} tickets for a total of: £{winnings}')

    elif intersection(num_list, ball_list) == 3:
        winnings += 30
        print(f'Player won £30 from: {count} tickets for a total of: £{winnings}')

    elif intersection(num_list, ball_list) == 4:
        winnings += 140
        print(f'Player won £140 from: {count} tickets for a total of: £{winnings}')

    elif intersection(num_list, ball_list) == 5:
        winnings += 1750
        print(f'Player won £1,750 from: {count} tickets for a total of: £{winnings}')

    if intersection(num_list, ball_list) == 6:
        winnings += 2000000
        print(f'Player won £2,000,000 from: {count} tickets for a total of: £{winnings}')
        quit()


