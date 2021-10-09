data_valid = False

while data_valid == False:
    grade1 = input("Type the grade of the first test: ")
    
    try:
        grade1 = float(grade1)
    except:
        print("Invalid input. Only numbers are accepted. Decimals should be separated with a dot.")
        continue
    
    if grade1<0 or grade1>10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    grade2 = input("Type the grade of the second test: ")
    
    try:
        grade2 = float(grade2)
    except:
        print("Invalid input. Only numbers are accepted. Decimals should be separated with a dot.")
        continue
    
    if grade2<0 or grade2>10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    total_classes = input("Type the total number of classes: ")

    try:
        total_classes = float(total_classes)
    except:
        print("Invalid input. Only numbers are accepted.")
        continue
    
    if total_classes<=0:
        print("The number of classes can't be zero or less")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    absences = input("Type the number of absences: ")

    try:
        absences = float(absences)
    except:
        print("Invalid input. Only numbers are accepted.")
        continue
    
    if absences<0 or absences>total_classes:
        print("The number of absences can't be less than zero or greater than the number of total classes")
        continue
    else:
        data_valid = True
data_valid = False
