print("choose operation")
print("1.addition")
print("2.substract")
print("3.multiplication")
print("4.divide")
print("5.percentage")

# Choose operation 
ch = int(input("Choose an operation (1-5): ")) 

# Input first number
a = float(input("Enter the first number: ")) 
# Input second number
b = float(input("Enter the second number: "))

# For operations needing second number 
if ch == 1: 
    print("Result:", a+b) 

elif ch == 2: 
    print("Result:", a-b) 

elif ch == 3: 
    print("Result:", a*b) 

elif ch == 4: 
    print("Result:", a/b) 

elif ch == 5: 
    print("Result:", a%b) 

else:
    print("invalid input:")    


