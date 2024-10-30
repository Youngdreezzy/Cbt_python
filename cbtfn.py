# CBT app with Functions

num_users = int(input('How many users are taking the Test: '))
allstudents = []
studentscores = []

for user in range(num_users):
    name = input(f'Name of Student {user + 1}: ')
    allstudents.append(name)

def Questions():
    questions = [
        '1) How many minutes are in an hour? a) 10 b) 12 c) 60:',
        '2) What is the smallest U.S. state by area? a) Texas  b) Los Angeles  c) Rhode Island: ',
        '3) How many dots appear on a pair of dice? a) 50  b) 70  c) 42: ',
        '4) What phone company produced the 3310? a) Samsung  b) Nokia  c) iPhone:',
        '5) What is the world’s largest retailer? a) Shoprite  b) Walmart  c) JustRite: '
    ]

    answers = ['c', 
               'c', 
               'c', 
               'b', 
               'b'
                ]

    for name in allstudents:
        score = 0  # Reset score for each student
        print(f"\n{name}, please answer the following questions:")

        for quest, ans in zip(questions, answers):
            print(quest)
            answer = input('Answer: ')
            
            if answer.lower() == ans:
                print('Correct')
                score += 5
            else:
                print('Wrong')

        print(f'\n{name}, your final score is: {score} / 25')
        studentscores.append(score)
        print('--' * 50)

    overall()

def overall():
    # Display all students' final scores
    print("\nFinal Scores:")
    for i in range(len(allstudents)):
        print(f'{allstudents[i]} => {studentscores[i]} / 25')

   
    index_min = studentscores.index(min(studentscores))
    print(f'The student with the minimum score is : {allstudents[index_min]}')

    index_max = studentscores.index(max(studentscores))
    print(f'The student with the maximum score is : {allstudents[index_max]}')


Questions()
