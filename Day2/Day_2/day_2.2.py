surname = "aludauri"

#პირველი ასოს გადიდება (კაპიტალუად ქცევა)
print(surname.capitalize())

#ყველა ასოს გადიდება
print(surname.upper())

#რომელიმე ასოს ჩანაცვლება
print(surname.replace("l","Q"))

name = "   David"

#სახელს ჩამოაჭრის სფეისებს
print(name.strip(), surname)

#როგორ დავშალოთ წინადადება სიტყვებად და შევქმნათ მათი სია
my_text = "I love sweden"
print(my_text.split())
#რასაც ფრჩხილებში ჩავუწერთ იმის მიხედვით გახლეჩს
print(my_text.split("l"))