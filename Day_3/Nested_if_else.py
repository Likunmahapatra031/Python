height=int(input("What is your height?"))
if height>=120:
    print("you can ride rollercoaster")
    age=int(input("what is your age/"))
    if age<12:
        print("pay $5")
    elif age<=18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print(" sorry, you can not ride rollercoaster..")
 