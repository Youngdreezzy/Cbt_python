# CBT Question and answer with modularization

# Importing another module 
from getPercent import get_percent

quest_ans = {
    '1. What is the capital of Nigeria a. Tokyo b. Abuja c. Accra':'b',
    '2. What is the capital of japan a. Tokyo b. Abuja c. Accra': 'a',
    '3. What is the capital of Ghana a. Tokyo b. Abuja c. Accra': 'c'
}

student_db = []

def registerStudent():
    global student_db

    while True:
        info = {
            'fullname':input('Fullname: '),
            'score':0
        }

        student_db.append(info)
        user = input('Press 1 to stop or Enter to continue: ')
        if user == '1':
            break
        else:
            continue

    print('Registration Successful ...')
    print(student_db)
    dashboard()

def dashboard():
    print(
        '''
    Welcome to myCBT APP

    1. Register Student 
    2. View Result
    3. Take Test
    #. Exit

    '''
    )
    option = input('Option: ')
    if option == '1':
        registerStudent()
    elif option == '2':
        resultStatistic()
    elif option == '3':
        takeTest()
    elif option == '#':
        exit()
    else:
        print('error')
        dashboard()
    


def resultStatistic():
    global student_db
    
    scores = []

    if not student_db:
        print('No Student found kindly register students ...')
        registerStudent()

    print('Student result ...')
    for student in student_db:
        print(f"\nfullname: {student['fullname']}\nScore: {get_percent(student['score'], 15)}%\n")
        scores.append(student['score'])

    max_score = max(scores)
    index_maxscore = scores.index(max_score)
    max_student = student_db[index_maxscore]
    print(f"{max_student['fullname']} got the highest score")

    min_score = min(scores)
    index_minscore = scores.index(min_score)
    min_student = student_db[index_minscore]
    print(f"{min_student['fullname']} got the lowest score")

    mean_score = sum(scores)
    lenght = len(scores)
    mean = mean_score/lenght
    print(f"The mean score is: {mean}")
    dashboard()


def takeTest():
    global student_db
    if quest_ans:
        print('Questions are available')
        if student_db:
            print('Time to take the test ...')
            for student in student_db:
                print(f"{student['fullname']}, Its time for your test ...")
                for ques, ans in quest_ans.items():
                    print(ques)
                    user_ans = input('Answer: ')
                    if user_ans.strip().lower() == ans:
                        print('correct')
                        student['score'] += 5
                    else:
                        print('wrong')
                print(f"Test completed. Score = {student['score']}")

            print(student_db)
            dashboard()
        
        else:
            print('No student found kindly register students ...')
            registerStudent()

    else:
        print('No question available ..')
        dashboard()

# dashboard()



# FOR CLASS IMPLEMENTATION

class Exam:
    def __init__(self) -> None:
        self.quest_ans = {
    '1. What is the capital of Nigeria a. Tokyo b. Abuja c. Accra':'b',
    '2. What is the capital of japan a. Tokyo b. Abuja c. Accra': 'a',
    '3. What is the capital of Ghana a. Tokyo b. Abuja c. Accra': 'c'
    }

        self.student_db = []   

    def dashboard(self):
        print(
        '''
    Welcome to myCBT APP

    1. Register Student 
    2. View Result
    3. Take Test
    #. Exit

    '''
    )
        option = input('Option: ')
        if option == '1':
            self.registerStudent()
        elif option == '2':
            self.resultStatistic()
        elif option == '3':
            self.takeTest()
        elif option == '#':
            exit()
        else:
            print('error')
            self.dashboard()

    def registerStudent(self):
        if not self.student_db:
            print('No Student found kindly register students ...')
            registerStudent()

        print('Student result ...')
        while True:
            self.info = {
            'fullname':input('Fullname: '),
            'score':0
            }
            self.student_db.append(self.info)
            self.user = input('Press 1 to stop or Enter to continue: ')
            if self.user == '1':
                break
            else:
                continue

        print('Registration Successful ...')
        print(self.student_db)
        self.dashboard()

    def takeTest(self):
        self.student_db
        if self.quest_ans:
            print('Questions are available')
            if self.student_db:
                print('Time to take the test ...')
                for student in self.student_db:
                    print(f"\n{student['fullname']}, Its time for your test ...")
                    for ques, ans in self.quest_ans.items():
                        print(ques)
                        user_ans = input('Answer: ')
                        if user_ans.strip().lower() == ans:
                            print('correct')
                            student['score'] += 5
                        else:
                            print('wrong')
                    print(f"Test completed. Score = {student['score']}")

                print(self.student_db)
                dashboard()
        
            else:
                print('No student found kindly register students ...')
                self.registerStudent()

        else:
            print('No question available ..')
            self.dashboard()

    def resultStatistic(self):
        self.scores = []

        for student in self.student_db:
            print(f"\nfullname: {student['fullname']}\nScore: {get_percent(student['score'], 15)}%\n")
            self.scores.append(student['score'])

        max_score = max(self.scores)
        index_maxscore = self.scores.index(max_score)
        max_student = self.student_db[index_maxscore]
        print(f"{max_student['fullname']} got the highest score")

        min_score = min(self.scores)
        index_minscore = self.scores.index(min_score)
        min_student = self.student_db[index_minscore]
        print(f"{min_student['fullname']} got the lowest score")

        mean_score = sum(self.scores)
        lenght = len(self.scores)
        mean = mean_score/lenght
        print(f"The mean score is: {mean}")
        self.dashboard()

test1 = Exam()
# To add to the initial question
test1.quest_ans.update({'4. What is the capital of Turkey a. Ankara b. Lace c. Buba': 'a'})

# To overwrite the code 

# test1.quest_ans = {'4. What is the capital of Turkey a. ankara b. Lace c. Buba ': 'a'}
# print(test1.quest_ans)

test1.dashboard()