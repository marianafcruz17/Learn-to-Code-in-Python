person = {"name": "Mariana Cruz","gender":"F","age":"23","address":"Rua 9 Norte - Aguas Claras","phone":"(61)99275-4180"}

key = input("What information do you want to know about the person? ")

result = person.get(key,"That information is not available")
print(result)
