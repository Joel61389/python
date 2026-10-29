#list datastructure
#changeable/mutable
#ordered/indexed
myproducts=["Bread" , "Milk" , "Sugar" , "Blueband"]
print(myproducts)
myproducts.pop()
# myproducts.append
myproducts[1]="honey"

print(f"i like drinking tea that has {myproducts[1]}")
print(myproducts)

# Tuple datastructures
# ordered has inedexes
# unchangeable/immutable
countrys=("kenya","Tanzania","Burundi","Somalia","Rwanda")
# countrys[0]="usa"
print(countrys)

# set datastructures
#avoid duplicates
#non ordered
computers={"hp","lenovo","dell","hp"}
print(computers)

#dictionary datastrucrure
customer={
    "name":"Erick",
    "Age":30,
    "city":"Nairobi",
    "salary":3000000,
    "proffesion":"software engoneer"


}
print(f"customer name : {customer['name']}")

myfruits=["mangoes","oranges","pineapples","watermelon", "avocado"]
for m in myfruits:
    print(f"I have {m}")
#imagine you are building as 
#school system that calculates the average marks 

marks = [65,89,64,89,90]
total =0
for x in marks:
    total=total+x
average=total/len(marks)
print(f"Total marks {total}")
print(f"Average marks {average}")

# create a complex calculator using
#craete inputoutput and controlflows

a=float(input("Enter a number :"))
b=float(input("Enter another number :"))
o=input("Enter an operator of your choice (+,-,*,/,%,**) :")

if (o == "+"):
    print(f"The answer is {a+b}")

elif(o == "-"):
    print(f"The answer is {a-b}")

elif(o == "*"):
    print(f"The answer is {a*b}")

elif(o == "/"):
    if b==0:
        print("You can't didvide with a zero")


    else:
        print(f"The answer is {a/b}")

elif(o == "%"):
    print(f"The answer is {a%b}")

elif(o == "**"):
    print(f"The answer is {a**b}")

else:
    print("The operand is invalid")