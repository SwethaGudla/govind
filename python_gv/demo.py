no=int(input('enter number'))
if no>1:
    for i in range(2,no):
        if(no%i)==0:
            print('not  a primenumber',no)
            break
    else:
        print('primenuber')# prime num progrm



