import time
import os
os.system('cls')

#1
'''def add(x, y):
    return y + x

print(add(3, 3))

print("Skriv in ditt tal ")

#2
def getname(name):
    return name

print(getname("Simon"))

#3

def add(x, y):
    return x + y
for i in range(10):
    print(add(20,10))'''

#4
'''def my_function():
    print(a)
    b=input("Vill du ta bort något i listan j/n? Eller skriv bara ett namn som borde läggas till: ")
    if b=="j":
        print(a)
        try:
            tabort=int(input(f"Vilket namn vill du ta bort 1-{len(a)}?: "))
            a.pop(tabort-1)
        except:
            print("Använd nummer tack")
    elif b=="n":
        print("hejdå")
        quit()
    else:
        a.append(b)
        print("ditt namn är tillagt")

a=["Eric", "Simon", "Peter"]
while True:
    my_function()'''

#5
def wait():
    time.sleep(0.2)

def math(x,y,type):
    if type=="+":
        answer=x + y
    elif type=="-":
        answer=x-y
    elif type=="*":
        answer=x*y
    elif type=="/":
        answer=x/y
    print(f"{x} {type} {y} = {answer}")

while True:
    type=input(f"\n            +  -  *  /\n\nVilken vill du använda?")
    acceptable = "+ - * / "
    if type not in acceptable:
        print(f"\nAnvänd +-/")
        wait()
    else:
        x= int(input(f"Välj x   x{type}y: "))
        y= int(input(f"Välj y   x{type}y: "))
        math(x,y,type) 
        wait()
        igen=input("Vill du köra igen j/n?: ")
        if igen=="n":
            quit()
