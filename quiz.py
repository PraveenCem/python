'''
    A mini quiz game where questions and options 
    will be shown. Based on the correct number of
    answers, scores will be displayed.
'''

import sys
def quiz():
    questions = ('Which is faster light or ferrari ?', 
                'Fastest bird ?',
                'Real Madrid is a club in a country ?',
                'Cheetah or leopard which is faster ?')
    options = (('a. Ferrari','b. Light'),
            ('a. Falcon','b. Penguin'),
            ('a. England','b. Spain'),
            ('a. Cheetah','b. Leopard'))
    answers = ('b','a','b','a')
    file_path = 'score.txt'
    try:
        with open(file_path,'r') as file:
            best_score = float(file.read())
    except FileNotFoundError:
        best_score = 0

    while True:
        guesses = []
        score = 0
        question_num = 0

        for question in questions:
            print(question)
            for option in options[question_num]:
                print(option)
            guess = input('Please enter your answer: ')
            guesses.append(guess)
            if guess.lower() == answers[question_num]:
                print('Correct')
                score += 1
            else:
                print('Incorrect')
                print(f'The correct answer was: {answers[question_num]}')
            question_num += 1
        score = score/len(questions)*100
        if score > best_score:
            best_score = score
        print(f'Your score is {score}%')
        print(f'Your best score is {best_score}')
        try:
            with open(file_path,'w') as file:
                file.write(str(best_score))
        except FileNotFoundError:
                best_score = 0
        if input('Please enter y to continue and n to quit : ').lower() == 'y':
            continue
        else:
            print(f'Thanks for playing!')
            break

############## CALL QUIZ PROGRAM

quiz()