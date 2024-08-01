for counter in range(0,20):
    sum=0
    num1=float(input("please enter num1?"))
    num2=float(input("please enter num2?" ))
    operation=input("please enter + or - or * or /?")
    if operation== "+":
        sum=num1 + num2
    elif operation=="-":
        sum=num1 - num2
    elif operation=="*":
        sum=num1 * num2
    elif operation=="/":
        sum=num1 / num2
    print(sum)


