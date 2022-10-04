age= int(input("Enter your age"))
# print(age)


if age<=5:
    print("you are baby ")
    if age>=1 and age <=3:
        print("you are nano")
    else:
        print("you are prebaby")
elif age>=6 and age<=12:
    print("you are child ")
    if age >= 6 and age <= 8:
        print("you are prechild")
    elif age >= 9 and age <= 10:
        print("you are middlechild")
    else:
        print("you are finalchild")
elif age>=13 and age<=40:
    print("you are adult ")
    if age >= 13 and age <= 25:
        print("you are preadult")
    elif age >=26 and age <= 35:
        print("you are middleadult")
    else:
        print("you are finaladult")
else:
    print("you are old")