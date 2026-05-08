def add(P,D):

    return(P+D)

def substract(P,D):
    return(P-D)

def multiply(P,D):
    return(P*D)

def divide(P,D):
    return(P/D)


print("Please select the operation:")
print("a. add")
print("b. substract")
print("c. multiply")
print("d. divide")

choice= (input("Enter your choice :"))

num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))

if choice=="a":
    print(num1,"+",num2,"=",add(num1, num2))

elif choice=="b":
    print(num1,"-",num2,"=",substract(num1,num2))

elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice =="d":
    print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("invalid input")
