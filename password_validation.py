L,U,D,S=0,0,0,0
Password=input("Enter a Password:")
Upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower_case="abcdefghijklmnopqrstuvwxyz"
Digits="0123456789"
Special_char="!@#$%&"
if  10 >= len(Password) >= 6:
    for i in Password:
        if i in Upper_case:
            U+=1
        if i in Lower_case:
            L+=1
        if i in Digits:
            D+=1
        if i in Special_char:
            S+=1
if U>=1 and L>=1 and D>=1 and S>=1:
    print("Password is valid")            
else:
    print("Password is not valid")
                    
