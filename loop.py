# for loop

for i in range(1,11):
    print(f"Welcome to my shop! {i}")
customers=["Erick","Angel","cynthia","joel","Linet"]
for c in customers:
    print(f"Welcome to todays class! {c}")

# calculate expense that you bought
# bread ksh.90
# milk ksh.120
# sugar ksh.160
my_shopping = [90,120,160]
total=0
for m in my_shopping:
    total=total+m
print(f"My total shopping cost is {total}")   

#imagine you have five customers and each pay you 100.create a
#script to get the total

total =0
for num in range (1,6):
    total=total+100
print(f"Total money collected : ksh.{total}")

#while loop

x=0
while x<=10:
    print(f"Loops {x}")
    x+=2    


# imagine you want save starting 0 balance
# and save 100 daily until 1000

money = 0
while money<1000:
    money=money+100
    print(f"MOney saved : {money}")   
print("Congratulations! You have reached your target")