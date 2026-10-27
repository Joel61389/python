# # a python program that checks if someone is eligible to vote or not

# age = int(input("Enter your age"))
# if age >=18:
#     print("you are eligible to vote")

# else:
#     print("you are not eligible to vote...you are underage")    


# # create a number program that checks if a number is odd or even    

# num = int(input("enter a random number :   "))
# if (num % 2==0):
#     print("The number is even")
# else:
#     print("The number is odd")

# # create a program that checks between 3 numbers which one is the biggest
# #method 1:using the control statement
# num1 = int(input("Enter a first number  :"))
# num2 = int(input("enter a second number :"))
# num3 =int(input("Enter a second number :" ))    

# if ((num1 > num2 )& (num1 > num3)):
#     print(f"The largest number is {num1}")

# elif ((num2 > num1) & (num2 > num3)):
#     print(f"The largest number is {num2}")

# else :
#     print(f"The largset number is {num3}")



# # method 2:using the built in max() function in python

# num1 = int(input("Enter a first number  :"))
# num2 = int(input("enter a second number :"))
# num3 =int(input("Enter a second number  : " ))  

# largenum = max(num1 , num2 , num3)

# print(f"The largest number of the three you entered is {largenum}")


#addition,subtraction,multiply,divisio
# num1 = float(input("Enter a first number  :"))
# num2 = float(input("enter a second number :"))

# print(f"Adding the two numbers the result is {num1+num2}")
# print(f"multiplying the two numbers the result is {num1*num2}")
# print(f"subracting the two numbers the result is {num1-num2}")
# print(f"dividing the two numbers the result is {num1/num2}")

# grading system

# grade = float(input("enter the students grade :"))
# if (grade <0 or grade >100):
#     print("invalid input")

# elif grade >= 70:
#     print("A")
        
# elif grade >= 60:
#     print("B")
# elif grade >= 50:
#     print("C")
# elif grade >= 40:
#     print("D")
# else:
#     print("FAIL")


#ELECTRICITY BILL CALCULATOR
#WRITE A PROGRAM THAT CALCULATES THE ELECTRICITY BILL BASED ON THE NUMBER OF UNITS CONSUMED. THE BILLING RATES ARE AS FOLLOWS:
#- For the first 100 units: 25 per unit
#- For the next 100 units (101-200): 35 per unit
#- For the next 100 units (201-300): 45 per unit

num_units = float(input("Enter the number of units bought :"))
if (num_units < 0):
    print("invalid input")

elif (num_units<=100):
     bill = num_units * 25
     print(f"Your bill is {bill}")

elif(num_units<=200):
    bill = (100 * 25) + ((num_units - 100) * 35)
    print(f"your bill is {bill}")
    

elif(num_units<=300):
    bill = (100 * 25) + (100 * 35) + ((num_units - 200) * 45)
    print(f"your bill is {bill}")


else: (num_units>300)
print(f"your bill is {num_units*67}")



    