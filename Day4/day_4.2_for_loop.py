# for i in range(10):
#     print(i)
#### for loop შეგვიძ₾ია გამოვიყენოთ ლისთებში
# food = ["one", "two", 100]
# for x in food:
#     print(x)
# name = "david"
# for i in name:
#     print(i)
# i = 0
# name = "david"
# while i < len(name):
#     print(name[i])
#     i += 1

########### for -iT
# food = ["one", "two", 100]
# i = 0
# for i in food:
#     print(i)

############# while loop -ის საშუალებით
# food = ["one", "two", 100]
# i = 0
# while i < len(food):
#     print(food[i])
#     i += 1

##### range შეგვიძ₾ია განვსაზღვროთ კონკრეტული ინტერვალისთვის
# for i in range(10,20):
#     print(i)

############ რა ნაბიჯებით გვინდა i -ის გაზრდა:
# for i in range(10,20,2):
#     print(i)
#     if i == 16:
#         print("i გახდა 16")
# my_list = ["one", "two", 100, "kachapuri", "yava"]
# for i in my_list:
#     print(i)
#     if i == "two":
#         print("me miyvars two")
#         break
##### შეგვიძლია for loop რამდენიმე საფეხურად შეგვიძ₾ია გამოვიყენოთ
#და შეგეგი იქნება წყვილად
# list_1 = [1,2,3]
# list_2 = [4,5,6]
# for num in list_1:
#     for num2 in list_2:
#         print(num, num2)
######## good one
# my_list = ["david", "aludauri"]
# for i in my_list:
#     for x in i:
#         print(x)
#     print("\n")


#########################halilulia #######################################
text = input()
dict = {}
#your code goes here
L = len(text)
for i in range(L):
    dict[text[i]] = text.count(text[i])
print(dict)