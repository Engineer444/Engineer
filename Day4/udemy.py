# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# #Write your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
#   if add_pepperoni == "Y":
#     bill += 2
# elif size == "M":
#   bill += 20
#   if add_pepperoni == "Y":
#     bill += 3
# elif size == "L":
#   bill += 25
#   if add_pepperoni == "Y":
#     bill += 3
# if extra_cheese == "Y":
#   bill += 1
# print (bill)

################### 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
L1 = len(name1)
L2 = len(name2)
###TRUE
T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")
L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")

summ = str(T + R + U + E) + str(L + O + V +E)
print(summ)