input1 = int(input("Enter your first digit: "))
input2 = int(input("Enter your second digit: "))


def sub(a, b):
    return(f"The sum of {input1} and {input2}  is: ", a-b)
def add(a, b):
    return(f"The sum of {input1} and {input2} is: ", a+b)
def div(a, b):
    return(f"The division of {input1} and {input2} is: ", a/b)
def mul(a, b):
    return(a*b)

x = int(input("1: subtract \n 2: add \n 3: divide \n 4: multiply \n Enter your application: "))

if x == 1:
    print(sub(input1, input2))
elif x == 2:
    print(add(input1, input2))
elif x == 3:
    print(div(input1, input2))
else:
    print(f"The division of {input1} and {input2} is: ", mul(input1, input2))