# lists
# my_list = ["khinkali", "mwvadi", "qatami", "mwvadi"]
# print(my_list[1])

#changeable list
# my_list.append(True)
# print(my_list)

##სიაში შეიძლება ერთნაირი ელემენტებიც იყოს
###sets cant contain dublicate elements

# print(len(my_list))
# print(my_list[1:3]) #ამით ქმნის ახალ სიას
# print("khinkali" in my_list) ### checking existence of an element in a list
# my_list[3] = "lobiani"  #### replacing element in a list

### inserting elements

# my_list.insert(2, "sulguni")
#  # removing
#  my_list.remove("khinkali")
#  print(my_list)
#  del my_list
#  print(my_list)

 ###### სიის გასუფთავება ისე რომ სიას არ წაშლის
#  my_list.clear()

#### სიის დასორტირება (ზრდადობის ან კლებადობის მიხედვით)

# my_list.sort() #ზრდადობის მიხედვითაა
# my_list.sort(reverse=True) #კლებადობის მიხედვით სორტირება
# print(my_list)
my_children = ["giorgi", "levani", "ana", "bagrati", "beqa"]
my_children.append("anastasia")
favorite_child = my_children[1:4]
print(favorite_child)
