#task 1 pg77
#a adds items to the list
file=open("username.csv","a")
username = input("please enter username")
# adds the imput to the txt
file.write( username )
file.close()
#
#task 2 pg77
#sets password as world
password=("world123")
#task3 pg77
# lets the person in put a guess for the password
answer = input("enter password")
# if the answer matches the password then the file will open if not denide will apear
if answer == password:
#opens the csv file
    file = open("username.csv","r")
    print("correct")
    print(file.read())
else:
    print("denide")
#task4 pg77
#sets the counter to 0
i = 0
#if the counter is less then 10 the loop continues
while i <10:
# sets the varible "num" to the imput
    num=input("enter a number")
# changes the origninal varible to the number with a comma at the end
    num=num + ","
    file = open("number.csv","a")
    file.write(num)
    file.close
#adds 1 to the couter at the start
    i +=1

file = open("number.csv","r")
dataIn = (file.read())

#task5 pg77
myList = dataIn.split(",")
myList = [float(i) for i in myList]
print(myList)

#task6 pg77


