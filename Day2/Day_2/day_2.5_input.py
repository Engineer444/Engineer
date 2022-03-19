# # name = input("enter your name: ")
# # surname = input("enter your nurname: ")
# # print(name, surname)

# a = int(input("enter number1: "))
# b = int(input("enter n2: "))

# print(a + b)

#### using input clause with format function########
age = input("age: ")
name = input("name: ")
surname = input(" surname: ")
my_text = "hello {}, your surname is {} and your age is {}"

print(my_text.format(name,surname,age))
