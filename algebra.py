#function for adding numbers 
def add_num(n,m):
    return n+m

#function for subtracting numbers
def sub_num(n,m):
    return n-m

#function for multiplying numbers
def multiply_num(n,m):
    return n*m

print("-- Simple calculator --")
while 1:
   
    print("""
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Exit """)
    ch=int(input("Choose the operation you want to perform (1/2/3/4):"))

    if ch==4:
        print("Calculator Closed !!")
        break

    
    n=int(input("Enter a number:"))
    m=int(input("Enter a number:"))



    if ch==1:
        print("Result =",add_num(n,m))
    elif ch==2:
        print("Result =",sub_num(n,m))
    elif ch==3:
       print("Result =",multiply_num(n,m))
    
    else:
        print("invalid choice !!")


    
    





