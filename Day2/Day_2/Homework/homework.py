#თუ სახელში ორჯერ მეტჯერ აქვს ასო ი
# და გვარი მთავრდება შვილიზე
#და ქულა მეტია 50-ზე
#დაპრინტოს დაფორმატებული ტექსტით name, surname, grade 
#else (you lose, დაფორმატებული ტექსტი name, surname, grade)

name = input("enter your name: ")
surname = input("Enter your surname: ")
grade = input("enter your grade: ")
my_text = "{} {}, you win! your grade is: {}"
if int(name.count("i")) > 1 and surname[(int(len(surname))-5):] == "shvili" and grade > 50:
    print(my_text.format(name, surname, grade))
else:
    print(my_text.format(name, surname, grade))
