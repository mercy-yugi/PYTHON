#in multiple lines
a=33
b=200
if b>a: print("b is greater than a")
elif a==b: print("a is not equal to b")
else: print("a is greater  than b")
#combining if and else in one line
x=1
y=2
z=3
print("x") if x>y else print("y")
#printing all the three commands in one line
print("x") if x>y else print("=") if x==y else print("y")

if x>y and z>a:
#and is used to merge the two operations
    print("both conditions are true")
 #while executes a statement as long as a condition is true.
i=1
while i<6:
    print(i)
    i+=1
    #braek statement is used to stop the loop
i=1
while i<5:
    print(i)
    if i==3:
        break#continue is used stop the curren iteration an continue

    i+=1

i=1
while i<3:
    print(i)
    i+=1
#for is used for iterating over asequence.
fruit=["mango","banana","apple","grapes"]
for x in fruit:
 print(x)
 #for looping through character 
 for x in "apple":
     print(x)

#for stoopping the loop before it finishes the entire process.
for x in fruit:
    print(x)
    if x=="banana":
        break
#continue statement
for x in fruit:
    if x=="apple":
        continue
    print(x)

#range()returns a sequence of numbers, starting from 0 and increments by one,and ends at a specified number.
for x in range(3):
    print(x)
    

