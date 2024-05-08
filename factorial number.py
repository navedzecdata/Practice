num= int(input("Please Enter:  "))
fact=1

if num<1:
    print("The Number is Not Valid for factorial: ")
else:
    for i in range(1,num+1):
        fact*=i

print("The Number is", num ,"And the Factorial is", fact)