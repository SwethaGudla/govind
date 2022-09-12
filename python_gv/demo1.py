#fibonicci series      
##a=int(input("Enter the first number of the series "))
##b=int(input("Enter the second number of the series "))
##n=int(input("Enter the number of terms needed "))
##print(a,b,end=" ")
##while(n-2):
##    c=a+b
##    a=b
##    b=c
##    print(c,end=" ")
##    n=n-1

##def fib(no):
##    if(no<=1):
##        return no
##    else:
##        return(fib(no-1)+fib(no-2))
##no=int(input('enter number:'))
##for i in range(no):
##    print(fib(i))
##print('----------------------------------------------------------------------------------')
#facorial
##no=int(input('enter no'))
##fact=1
##for i in range(no):
##    fact=fact*no
##    no=no-1
##print(fact)
##print('-----------------------------------------------------------------------------')
###using recursion
##def fact(no):
##    if(no<=1):
##        return 1
##    else:
##        return (no*fact(no-1))
##no=int(input('enter nuber:'))
##print(fact(no))

start=int(input("enter starting range:"))
last=int(input("enter ending range:"))
for no in range(start,last+1):
    if no>1:
        for i in range(2,no):
            if(no % i)==0:
                break
        else:
            print(no)
    
      
      

      
      
      
    
