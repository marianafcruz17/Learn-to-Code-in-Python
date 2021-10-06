months = ("Janeiro","Fevereiro","Março","April","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
birthday = input("Type your birthday in the format DD-MM-YYYY ")

index = int(birthday[3:5]) - 1
bd_month = months[index]

print("You were born in ",bd_month)





people = ["Mariana", "Isadora", "Maria", "Gilson"]

user = input("Type your name: ")

people.append(user)
print("Here's the list: ",people)
