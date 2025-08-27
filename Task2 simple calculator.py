print("choose operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Percentage")

# Choose operation 
ch = int(input("Choose an operation (1-5): ")) 

# Input first number
a = float(input("Enter the first number: ")) 
# Input second number
b = float(input("Enter the second number: "))

#perform calculation
if ch == 1: 
    print("Result:", a+b) 

elif ch == 2: 
    print("Result:", a-b) 

elif ch == 3: 
    print("Result:", a*b) 

elif ch == 4: 
   if b !=0:
    print("Result:", a/b) 
   else:
       print("Error :Division by zero is not allowed")

elif ch == 5: 
    if b !=0:
        Percentage =(a/b)*100
        print("Percentage:",
             round(Percentage,2),"%") 
    else:
       print("Error :Total value cannot be zero")

else:
    print("invalid input:")    



