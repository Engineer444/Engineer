######### რიცხვების შედარება
def comparison(num1, num2):
    if num1 > num2:
        print("the largest number " + str(num1))
        return num1
    else:
        print("the largest number " + str(num2))
        return num2
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
max1 = comparison(num1, num2)

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
max2 = comparison(num1, num2)

print(max1 + max2)
