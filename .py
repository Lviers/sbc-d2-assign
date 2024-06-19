from random import randint

num1 = int(input("Enter your first number!!: "))
num2 = int(input("Enter your second number!!: "))
num3 = int(input("Enter your third number!!: "))


gamblingaddiction = False

while not gamblingaddiction:

    res1 = randint(0,9)
    res2 = randint(0,9)
    res3 = randint(0,9)

    print("Your swertres number!!: ", num1, num2, num3)
    print("Result of the Day!!(?): ", res1, res2, res3)

    if num1 == res2 and  num2 == res3 and  num3 == res3:
        print("You've won a gazillion dollars!!!")
        gamblingaddiction = True

    elif (num1 == res2 and  num1 == res3 and  num1 == res3) or (num2 == res2 and  num2 == res3 and  num2  == res3) or (num3 == res2 and  num3 == res3 and  num3  == res3):
        print("You partially win!")
    else:
        print("you lose")
