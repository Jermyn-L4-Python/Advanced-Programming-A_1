import random

def displayMenu():
    #Easy = Single Digit Numebers, Moderate = Double Digit, Advanced = 4 Digit

    print("Welcome to the Math Quiz! \nChoose your difficulty level (1, 2, 3): \n1. Easy \n2. Moderate \n3. Advanced")

    choice = int(input(""))
    return choice


def randomInt(level):
    if level == 1:
        return random.randint(1, 9)

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(1000, 9999)


def decideOperation():
    return random.choice(['+', '-'])


def displayProblem(level):
    num1 = randomInt(level)
    num2 = randomInt(level)
    operation = decideOperation()

    answer = int(input(f"{num1} {operation} {num2} = "))

    if operation == "+":
        correct = num1 + num2
    else:
        correct = num1 - num2
    
    return answer, correct


def isCorrect(answer, correct):
    if answer == correct:
        print("WOW! You are Correct!!!")
        return True
    else:
        print("Aww, you are wrong :(")
        return False


def displayResults(scores):
    print(f"Score: {scores}/100")
    if scores >= 90:
        print("AMAZING! You're an A+!")
    elif scores >= 80:
        print("Good work! You're an A!")
    elif scores >= 70:
        print("Almost there! You're a B!")
    else:
        print("Better luck next time, You're a C.")



while True:
    scores = 0
    attempts = 10

    level = displayMenu()  
    
    for i in range(attempts):
        print(f"Question {i+1}: ")

        answer, correct = displayProblem(level)

        if isCorrect(answer, correct):
            scores+=10
        else:
            answer = int(input("Incorrect, try again: "))
            if isCorrect(answer, correct):
                scores+=5

    displayResults(scores)

    again = input("Play again? Y or N: ")
    if again.capitalize() != "Y":
        print("Thank you for playing!")
        break









