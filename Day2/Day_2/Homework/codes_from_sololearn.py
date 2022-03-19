######## breaking ###############
# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if i >= 5:
#     print("Breaking")
#     break
# print("Finished")
############ my example for break ############
# i = 10
# while True:
#   print (i)
#   i -= 1
#   if i < 0:
#     print("finished")
#     break
########## breaks and continue problem
# total = 0
# while True:
#     p1 = int(input("enter your age: "))
#     p2 = int(input("enter your age: "))
#     p3 = int(input("enter your age: "))
#     p4 = int(input("enter your age: "))
#     p5 = int(input("enter your age: "))
#     total += 100
#     if p1 < 3 or p2 < 3 or p3 < 3 or p4 < 3 or p5 < 3:
#         continue
#     if total > 500:
#         break
#     print(total)

#################another problem: #####################
# weight = float(input("enter weight: "))
# height = float(input("enter your height: "))
# BMI = weight/height

# if BMI < 18.5:
#     print("Underweight")
# elif BMI < 25 and BMI >= 18.5:
#     print("Normal")
# elif BMI < 30 and BMI >= 25:
#     print("Overweight")
# else:
#     print("Obesity")

####################lists #########
# nums = [1,2,3,4,5]
# nums2 = ["a", "b", "c"]
# matrix1 = [
#   [1,2,3,4],
#   [3,4,6,9]
# ]
# print(matrix1[0][2])
# things = ["text", 0,[1, 2, 8], 4.56]
# print(things[2][2])
# num1 = [1,2,3,4,5]
# num2 = [2,5,4,3,7]
# print(num1 * 2)
# words = ["spam", "egg", "spam", "sausage"]
# print("spam" in words)
# print("egg" in words)
# print("tomato" in words)
# x = "hello world"

# if "world" in x:
#   print("Yes")
# nums = [1, 2, 3]
# print(not 4 in nums)
# print(4 not in nums)
# print(not 3 in nums)
# print(3 not in nums)
########## fifferent loops
# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#   print(word + "!")
# list1 = ["a", "b", "c"]
# for x in list1:
#   print(x*2)
########### another example
# str = "i love sweden"
# count = 0
# for x in str:
#   if(x == 'e'):
#     count += 1
# print(count) 
############# continue and break for loop
# text = "i love sweden"
# for x in text:
#   if x == 'e':
#     break
#   print(x)
#   break
############ fo loop task
# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# summ = 0
# for y in x:
#   summ = summ + y 
# print(summ)

##### range
# numbers = list(range (10, 5, -2))
# print(numbers)
####### for loop & range
# for i in range(3):
#   print("Hello!")

#### LIST SLICES ######
# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[::-1])
####input a string and output the last character of it
# string = input()
# string2 = string[::-1]
# print(string2[0])
# print()
########quiz
# list = [1,2,3,4,5,6,7,8,9]
# print(list[list[4]])

#######sum of consecutive numbers ######
N = int(input())
summ = 0
range1 = list(range(N+1))
for i in range1:
    summ += i
print(summ)
