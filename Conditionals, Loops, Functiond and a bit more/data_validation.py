data_valid = False

while data_valid == False:
    grade1 = float(input("Type the grade of the first test: "))
    if grade1<0 or grade1>10:
        print("Grase should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    grade2 = float(input("Type the grade of the second test: "))
    if grade2<0 or grade2>10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    total_classes = int(input("Type the total number of classes: "))
    if total_classes<=0:
        print("The number of classes can't be zero or less")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    absences = int(input("Type the number of absences: "))
    if absences<0 or absences>total_classes:
        print("The number of absences can't be less than zero or grea")
        continue
    else:
        data_valid = True
data_valid = False
