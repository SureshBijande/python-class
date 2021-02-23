#Python Program to Make a Simple Calculator by using Functions.

def add(a,b):
    '''This function adds two numbers'''
    sum = a+b;
    return sum;

def sub(a,b):
    '''This function subtracts two numbers'''
    subs =  a-b;
    return subs;

def mul(a,b):
    '''This function multiplies two numbers'''
    mult = a*b;
    return mult;

def div(a,b):
    '''This function divides two numbers'''
    divi = a/b;
    return divi;

def power(a,b):
    '''This function return power'''
    pows = pow(a,b);
    return pows;

#Take inputs from user.

print("Select Operation.")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Power")

choice = input("Enter Choice(1/2/3/4/5):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2,"=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2,"=", sub(num1,num2))

elif choice == '3':
    print(num1, "*", num2,"=", mul(num1,num2))

elif choice == '4':
    print(num1, "/", num2,"=", div(num1,num2))

elif choice == '5':
    print(num1, "^", num2,"=", power(num1,num2))

else:
    print("Invalid Input")
