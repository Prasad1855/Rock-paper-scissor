print("""List of operations: 
       1.Add,Subtract,Multiply,Divide
       2.Average
       3.Square,Square root 
       4.Percentage
       5.Temperature conversion 
       6.Currency conversion
       """  
)
operation=int(input("Select opeartion:"))
if operation==1:
    print("""Select from below:
             1.Add
             2.Subtract
             3.Multiply
             4.Divide"""  )
    choice=int(input("Select operation:")) 
    num1=int(input("Enter first number:"))    
    num2=int(input("Enter second number:"))
    if choice==1:
        print(num1,"+",num2,"=",num1+num2)    
    elif choice==2:
        print(num1,"-",num2,"=",num1-num2)    
    elif choice==3:
        print(num1,"*",num2,"=",num1*num2)
    elif choice==4:    
        print(num1,"/",num2,"=",num1/num2)        
    else:
        print("Invalid")    

elif operation==2:
    n=int(input("Enter the total number you want to enter:")) 
    sum=0
    for i in range(n):
        x=int(input("Enter the numbers:"))
        sum+=x
    Avg=sum/n
    print("Average is :",Avg)   

elif operation==3:
    print("""Select from below:
              1.Square
              2.Sqaure root""")     
    choice=int(input("Select  :"))  
    n=int(input("Enter a number:"))
    if choice==1:
        print("Square of",n,"is :",n*n)  
    elif choice==2:
        print("Square root of",n," is :",n**0.5) 
    else:
        print("Invalid")    

elif operation==4:
    num1=int(input("Enter part number:"))
    num2=int(input("Enter a base number:"))
    percentage=(num1/num2)*100
    print("Percentage :",round(percentage),"%")

elif operation==5:
    print("""Select from below:
             1.Celcius to Fahrenheit
             2.Fahrenheit to Celcius""")
    choice=int(input("Select 1 or 2 :  "))      
    if choice==1:   
       C=float(input("Temperature value in degree celcius :"))
       C_to_F=(C*1.8)+32
       print("The", C,"degree celcius is equal to: ",C_to_F,"fahrenheit")  
    elif choice==2:
        F=float(input("Temperature value in degree fahrenheit:"))    
        F_to_C=(F-32)/1.8
        print("The",F,"degree fahrenheit is equal to:",F_to_C,"celcius")      

elif operation==6:
    print("""Select conversion:
             1.USD to INR
             2.INR to USD
             3.Pound to INR
             4.INR to pound""" )
    choice=int(input("select from 1,2,3,4 : "))
    if choice==1:
        n=int(input("Enter a amount in USD : "))
        USD_to_INR=n*80
        print("The",n,"$ is equal to:",USD_to_INR,"Rs")
    elif choice==2:
        n=int(input("Enter a amount in INR : "))
        INR_to_USD=n/80
        print("The",n,"Rs is equal to:",INR_to_USD,"$")    
    elif choice==3:
        n=int(input("Enter a amount in Pound : "))
        GBP_to_INR=n*96
        print("The",n,"£ is equal to:",GBP_to_INR,"Rs")     
    elif choice==4:
        n=int(input("Enter a amount in INR : "))
        INR_TO_GBP=n/96
        print("The",n,"INR is equal to:",INR_TO_GBP,"£") 

                    


