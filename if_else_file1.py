print("enter choice")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
user_choice=int(input("Enter your choice:  "))
if (user_choice==1):
    print("you have selected addition option")
    a=int(input("please enter the first number"))
    b=int(input("please enter the second number"))
    result=a+b
    print("addition of two numbers is : ",result)

elif (user_choice==2):
    print("you have selected subtraction option")
    a=int(input("please enter the first number"))
    b=int(input("please enter the second number"))
    result=a-b
    print("difference of two numbers is : ",result)

elif (user_choice==3):
    print("you have selected multiply option")
    a=int(input("please enter the first number"))
    b=int(input("please enter the second number"))
    result=a*b
    print("product of two numbers is : ",result)

elif (user_choice==4):
    print("you have selected division option")
    a=int(input("please enter the first number"))
    b=int(input("please enter the second number"))
    result=a/b
    print("result after division is : ",result)


else:
    print("please enter the valid input")



    