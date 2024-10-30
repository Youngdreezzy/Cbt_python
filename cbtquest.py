# CBT question and answer before FUNCTION learning 

num_students = int(input('How many Students are taking the Test: '))
allstudents = []
studentscores = []

for num in range(num_students):
    
    # Collecting student name
    name = input(f'Name of Student {num + 1}: ') 
    allstudents.append(name)



Questions = [
        '1. Which country has the highest life expectancy? a). Nigeria  b). Ghana c). Hong Kong', # C
        '2. How many minutes are in an hour? a). 10 b). 12 c). 60 ',       #C
        '3. How many dots appear on a pair of dice? a). 50  b). 70  c). 42',           #C
        '4. What phone company produced the 3310 a). Samsung  b). Nokia  c). iphone',      #B
        '5. What is the world’s largest retailer? a). Shoprite  b). Walmart  c). JustRite'     #B
]

answers =[
    'c',
    'c',
    'c',
    'b',
    'b'
]

# Dishing out the questions and options to each student and verifying the answers
for name in allstudents:
    print(f'{name}: Answer all the questions correctly and press enter after each answer.')
    score = 0

    for quest, ans in zip(Questions, answers):
        print(quest)
        answer = input('Answer: ')
        
        if answer == ans:
         print('Correct!')
         score += 5
        else:
            print('Wrong!')

    print(f'{name}, your final score is: {score} | 25')
    studentscores.append(score)
    print('-' * 50)

# Printing out the students final score 
print('Test complete for all students and here is the Final scores.')
for i in range(num_students):
    print(f'{allstudents[i]} => {studentscores[i]}')
print('-' * 50)

# Calculating the mean, minimum and maximum score of the student
length = len(allstudents)
sum_all = sum(studentscores)
mean = sum_all/length
print(f'The Mean Score is : {mean}')


minim = (min(studentscores))
print(f'Minimum Score is : {minim}')

minim = (max(studentscores))
print(f'Maximum Score is : {minim}')

# Identifying student with the minimum and maximum score
index_min = studentscores.index(min(studentscores))
print(f'The student with the minimum score is : {allstudents[index_min]}')

index_max = studentscores.index(max(studentscores))
print(f'The student with the maximum score is : {allstudents[index_max]}')



