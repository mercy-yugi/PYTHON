thisList=["apple", "banana","cherry"]
print(thisList)
#list length
print(len(thisList))
#using the list() constructor.
thislist=list(("apple","mango","banana"))
print(thislist)
#list-collection which is ordered and changeable. allows aduplicate
#tuple- collection which is ordered and unchangeable. allows duplicate
#set-collection which is unordered and changeable. no duplicate mebers
#dictionary-collection which is ordered and changeable.

#access items
print(thislist[1])
#negative indexing- starts from the end
print(thislist[-1])

#ranges of index
names=list(("mercy", "yugi","zuena","kiki","haki","cudra","swab"))
print(names[2:5])
print(names[:4])#highlights the items from the beginning t the fourth element
print(names[2:])#prints out all the names the third item to the end.
print(names[-4:-1])

#checks if item exists
if "yugi" in names:
    print("Yes, 'yugi' is in fruits list")

#changing the value of a specific item
cars=["mazda","toyota","subaru"]
cars[1]="benz"
print(cars)

#change a range of item values
cars[1:2]=["honda","mitsubishi"]
print(cars)

#inserting items
cars.insert(2,"tesla")
print(cars)

#.append() adds items to the end list
cars.append("fit")
print(cars)

#.insert() inserts item at the specified index
cars.insert(1,"mark x")
print(cars)

#.extend()- adds two lists to one 
cars.extend(names)
print(cars)

#removes specified item
cars.remove("mark x")
print(cars)

#removes spcified index. pop()
cars.pop(1)
print(cars)
#if index not specified, it deletes the lastitem
cars.pop()
print(cars)