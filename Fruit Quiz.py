import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {"apple": "red" ,"orange": "orange" , "watremelon": "green" , "banana": "yellow" ,  }
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_ans = input()
            if(user_ans.lower() == color):
                print("CORRECT ANSWER !")
            else:
             print("WRONG ANSWER !")
            option = int(input("Enter 0 , if you want to play again otherwise enter 1:"))
            if (option):
                break
print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()