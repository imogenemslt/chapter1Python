#recursion
#benifits= a function that calls its self,clean and eligent, breaks problems down into sub tasks
#disadvatages= cand be heavy on memory, can be hard to de bug
def factial(x):
    if x ==1:
        return 1
    else:
        return (x * factial(x-1))

num= int(input("enter your number"))
print("the factial of", num, "is", factial(num))
