blog_posts = ["","The 10 coolest math function in Python","","How to make HTTP requests in Pyton","A tutorial about data types"]

for post in blog_posts:
    if post=="":
        continue
    else:
        print(post)
        
print("-------------------------")
myString = "This is a string"

for char in myString:
    print(char)

print("-------------------------")

for x in range(0,10):
    print(x)

print("-------------------------")

person = {'Name': 'Mariana Cruz', 'Age': 23, 'Gender': 'Female'}

for key in person:
    print(key, ":", person[key])

print("-------------------------")

blog_posts = {"Python":["The 10 coolest math function in Python","How to make HTTP requests in Pyton","A tutorial about data types"],"JavaScript":["Namespaces in Javascript","New function avaliable in ES6"]}

for category in blog_posts:
    print("-> Posts about ", category)
    
    for post in blog_posts[category]:
        print(post)
    print("-------------------------")  
