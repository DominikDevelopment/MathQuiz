
points = 0
sendnow = False
maxpoints = 5
class Question:
    def __init__(self, Question, Answer):
        self.Question = Question
        self.Answer = Answer
        global points
        print(Question)
        entry = input('Answer = ')
        if entry == Answer: points = points + 1
print("""
                                RULES:
            You can use a paper and a pencil to calculate.
  You can NOT use a calculator, if you do it does not prove anything.
    If you find a bug contact Me at Dominik.PYDevelopment@gmail.com
                    Please give your actual name.
""")   
name = input("What is your name: ")
q1 = Question("(x * 2) + (5 * 2) = ", '16')
q2 = Question("[x - (5 + 3)] * 2 = 4", '12')
q3 = Question("5X + (5X - 1), X5 = 25", '49')
q4 = Question("[x + 2 * (4 + 2)] = 15", '3')
q5 = Question("(2 * 5) + (5 * [x + 2] + 2) = 37", '3')
precentage = 100/maxpoints * points
precentagestr = str(precentage)
pointstr = str(points)
print("You got " + pointstr + " Points That is ") 
print(precentagestr + "%")

 

if points == maxpoints: print('SUPER')
sendnow = True

