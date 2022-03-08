my_dict = {
    "name" : "davit",
    "surname": "aludauri",
    "age" : 25,
    "location": "Tbilisi",
    "children" : ["name1", "name2"]
}

#დამაბერეთ 10 წლით, 
# დამადეთ ახალი წყვილი has_gf:true
#ამოაგდეთ ლოკაცია
#გაასუფთავეთ
my_dict["age"] = 32
my_dict["has_gf"] = True
my_dict.pop("location")
print(my_dict)
# my_dict.clear()