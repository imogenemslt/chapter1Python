a=True
print(a)
luskcafes=5
rushcafes=8
print(luskcafes>rushcafes)
print((luskcafes==6)and(rushcafes==8))
answer=input("do you have a loyalty card?c(Y/N)")
if answer=="y":
    print("please scan your card.")
else:
    print("do you want to sight up for one?")

paytype=input("do you want to pay with card cash or coupon?")
if paytype=="cash":
    print("insert cash")
elif paytype=="card":
        print("insert card into machine.")
else:
    print("coupons are only accepted at customer service.")
            
# #task 4 page 31

ticket=input(" please enter your voucher code")
if ticket=="A":
    print("congratulations you won a ticket to dudrum shopping centre")
elif ticket=="B":
    print("congratulations you won a ticket to tallaght")
elif ticket=="C":
    print("congratulations you won a ticket to broombridge")
else:
    print("invalid code")
#task5 page 31
percent=input("enter in your percent")
if percent<="29":
    print("H8")
elif percent<="39":
    print("H7")
elif percent<="49":
    print("H6")
elif percent<="59":
    print("H5")
elif percent<="69":
    print("H4")
elif percent<="79":
    print("H3")
elif percent<="89":
    print("H2")
elif percent<="99":
    print("H1")
else:
    print ("error please enter valid percent")

