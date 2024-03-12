#--------------------FIBONACCI Series-------------------------------
def fibo(x,n):
    if x==0:
        return 0
    if x==1:
        return 1
    return fibo(x-1)+fibo(x-2)
#-------------------FACTORIAL of a Number-----------------------------
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
#------------------PALINDROME Checker--------------------------
def palin(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palin(s[1:-1])
        else:
            return False
#------------------ARMSTRONG Checker-----------------------------
def arms(num,n1,sum,temp):
    if temp==0:
        if sum==num:
            return True
        else:
            return False
    digit = temp % 10
    sum = sum + digit**n1
    temp = temp//10
    return arms(num, n1, sum, temp)      
#---------------------String REVERSE (Except special characters)----------------
def rev_str(x):
    i=0
    j=len(x)-1    
    while i!=j:
        if(x[i].isalpha() and x[j].isalpha()):
            x[i],x[j]=x[j],x[i]
            i+=1
            j-=1
        elif(not x[i].isalnum() and not x[j].isalnum()):    
            i+=1
            j-=1
        elif (not x[i].isalnum()):
            i+=1
        elif (not x[j].isalnum()):
            j-=1
    return x
#-------------------Print TRIANGLE Pattern------------------------------------
def print_space(space):
     
    # base case
    if (space == 0):
        return;
    print(" ", end = "");
    print_space(space - 1);
def print_asterisk(asterisk):
    if(asterisk == 0):
        return;
    print("* ", end = "");
    print_asterisk(asterisk - 1);
def pattern(n, num):
     
    # base case
    if (n == 0):
        return;
    print_space(n - 1);
    print_asterisk(num - n + 1);
    print("");
    pattern(n - 1, num);       
#---------------------------Sum of NATURAL Numbers-------------------------
def nat_sum(n):
   if n <= 1:
       return n
   else:
       return n + nat_sum(n-1)         
#------------------------------EVEN Numbers SUM---------------------------
def sum_of_even(n):
    if not n % 2 == 0:
        return n
    else:
        return n + sum_of_even(n-1)
#------------------------------ PRIME Numbers SUM------------------------
def prsum(p):
    sum=0
    for number in range(2, p+ 1):
         i = 2
         for i in range(2, number):
            if (int(number % i) == 0):
                i = number
                break;
         if i is not number:
            sum=sum + number
    return sum    

#-------------------------------ODD Numbers Sum-----------------------------
def sum_of_odd(n):
    if  n % 2 == 0:
        return n
    else:
        return n + sum_of_odd(n-1)