f = open("test.txt","r")
print(f.read())

f.write("This text will overwrite the content of our file")

f = open("test.txt")
print(f.read())

f = open("/Users/Maria/Deskto/myfile.txt","x")
