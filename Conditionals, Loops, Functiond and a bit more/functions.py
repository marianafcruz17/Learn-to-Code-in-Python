def say_hello(person):
    print("Hello!" + person + ", how are you doing? ")

say_hello("Mary")
say_hello("Paul")
say_hello("Kelly")

def fahr2celsius(fahr):
    celsius = (5*(fahr-32))/9
    return celsius

print("Celsius: ",round(fahr2celsius(100),2))
print("Kelvin: ",round(fahr2celsius(100)+273.5,2))
