###### ალგორითმი
#ალგორითმი არის ამოცანის ამოხსნისთვის საჭირო პროცესების მიმდევრობა
#ფუნქცია - არის ალგორითმი რომელსაც აქვს კონკრეტულის ახელი და არის
#ბreusable და იმით გამოირჩევა, რომ შეგვიძ₾ია სხვადასხვა არგუმენტებს
#მოვარგოთ
# def my_func(a,b,c):
#     return (a + b + c)/3
# x = input([])
# def my_func(x):
#     sum = 0
#     for i in range(len(x)):
#         sum += x[i]
#     return sum
# print(my_func(x))
################# ეს გავარჩიო კარგად:
def my_mean(arr):
    my_sum = 0
    for element in arr:
        my_sum += element
    return my_sum/len(arr)
arr = []
ammount_of_numbers = int(input("შეიყვანეთ რამდენი რიცხვის შეყვანა გსურთ: "))
for i in range(ammount_of_numbers):
    x = int(input("შეიყვანეთ რიცხვი " + str(i+1) + " სიისთვის: "))
    arr.append(x)
print(my_mean(arr))