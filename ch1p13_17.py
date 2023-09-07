#this is a single-line comand
"""
this is a multiline comment. it can have as
many lines as needed
"""
length=5
print (length)

x=5
#this is an integer (whole number)
y=3.14
#this is a float (decimal point)
z="pie"
#this is a string (words)
k = True
#this is a boolean (true or false)
print (type(x))
print (type(y))
print(type(z))
print(type(k))

#changing varible while program runs 
x=5
print(type(x))
x=5.2
print(type(x))

#converting a varible value to a float
x=float(5)
print(type(x))
print(x)
x=5.1
print(type(x))
print(x)

#converting a float to an int
x=float(5)
print(type(x))
x=int(5.1)
print(type(x))

#coverting any varible
myInt=int("5")
myFloat=float("5.5")
myString=str(5)
mybool=bool("False")

print(myInt)
print(myFloat)
print(myString)
print(mybool)

x=5
y=3
z=7
print("the answer is:",x,y,z)

#symbols for arithmetic operation
x=5
x=x+2
print(x)
x*=2
print(x)
#
pi=3.14
r=7
answer=((4/3)*pi)*r**3
print(answer)
# less decmils
pi=3.14
r=7
answer=((4/3)*pi)*r**3
answer=round(answer,2)
print(answer)
#string and string operators
myString="hello world"
print(myString)

string1="hello"
string2="world"
space=" "
answer=(string1+" "+string2 )*3
print(answer)
