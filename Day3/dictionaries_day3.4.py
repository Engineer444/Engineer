from re import M


my_dict = {
    "name" : "davit",
    "surname": "aludauri",
    "age" : 25,
    "children" : ["name1", "name2"]
}
#### dictionary is ordered, changeable, and no duplicates

print(my_dict)
print(len(my_dict)) #ამით ზომავს რამდენი წყვილია იმას

print(my_dict["children"][1]) # ასე შეგვიძლია მივწვდეთ ელემენტებს