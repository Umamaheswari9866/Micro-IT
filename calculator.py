import math
import random
def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
def power(x,y):
    return x**y
print("select operation-\n"
    "1.addition\n" 
    "2.subtraction\n"
    "3.multiplication\n"
    "4.division\n"
    "5.power\n")
sel=int(input("choose the operation(1-5) :"))
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
while True:
    if(sel==1):
        print(num1,"+", num2 , "=", add(num1,num2))
        break;
    elif(sel==2):
        print(num1,"-", num2 , "=", sub(num1,num2))
        break;
    elif(sel==3):
        print(num1,"*", num2 , "=", multiply(num1,num2))
        break;
    elif(sel==4):
        print(num1,"/", num2 , "=", div(num1,num2))
        break;
    elif(sel==5):
        print(num1,"^", num2 , "=", power(num1,num2))
        break;
    else:
        print(f"invalid input")
        break;
