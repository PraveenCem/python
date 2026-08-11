import random
def rock_paper_scissors():
    options = ('rock','paper','scissors')
    winning_moves = {'rock':'scissors',
                      'paper' :'rock',
                      'scissors' :'paper'}
    while True:
        
        user = input('please enter your choice(rock,paper,scissors): ').strip().lower()
        if user not in options:
            print('invalid choice')
            continue
        computer = random.choice(options)
        if user == computer:
            result = 'Draw'
        elif winning_moves[user] == computer:
            result = 'You Win'
        else:
            result = 'You Lose'
        print(f'{result}, computer chose {computer} and you chose {user}')

        if input('please enter y to continue and n to quit: ').strip().lower() == 'y':
            continue
        else:
            print('Thank you for playing!')
            break


rock_paper_scissors()