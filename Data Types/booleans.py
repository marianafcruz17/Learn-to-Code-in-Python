num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))

if(num1>num2):
    print(num1, " is greater than ",num2)
elif(num1==num2):
    print(num1," is equal to ",num2)
elif(num1<num2):
    print(num1," is less than ",num2)
    
print("This is out of the if structure")




age = 23

user_age = int(input("Type your age: "))

if(user_age>age):
    print("You're old than me")
elif(user_age==age):
    print("We're the same age")
elif(user_age<age):
    print("You're younger than me")
