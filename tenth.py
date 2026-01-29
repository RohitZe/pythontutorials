# while loop
# cnt=0
# while True:
#     print('print')
#     cnt=cnt+1
#     if cnt==5:
#         break




# print('loop breaked',cnt)
# break =exit from code on some condition

# hints -- palindrome--121
# number original number rev if rev==original then palidrome ,not palindrome
#factorial 5=5*4*3*2*1
#prime number jinke 2 se zada factor hote hai
#aese number jinke 1 or self ke alava koi factor nhi hota
# 2-->1,2 prime number-->smallest prime number
# 5 ---> prime number 1,5
# 7--->prime number
# 9 ----> 1,3,9
# logic--> 2---8--->flag=false prime no. 9 flag =true prime hai
# i/p->prime
# num=5
# i=2
# flag=True
# while i<num:
#     if num%i==0:

#         flag=False
#         break
#     i=i+1
    

# if flag:
#     print('i m a prime no')
# else:
#     print('not a prime no')

# num=596888
# maxi=999999
# while num>0:
#     rem=num%10
#     maxi=min(maxi,rem)
#     num=num//10

# print(maxi)

# 12634
# 6
# 1,2,3,6,4
# maxi=max(rem)
# maxi

# 120
# print all factors

# hcf gcd 
# 18,20
#  2->1,2
#  400->1,2,4,5,10,20

# factors print

# lcm 
# 4-> 4,8,12,16,20,24,28,32,36
# 6-> 6,12,18,24,30,36
# 13 17
# 13*17


# print(min(2,5))

# num1=2
# num2=20
# i=1
# gcd=1
# while i<=min(num1,num2):
#     if num1%i==0 and num2%i==0:
#         gcd=i
#     i=i+1
  
# print(gcd)

# lcm*hcf=product of two numbers
# lcm=num1*num2/hcf

num1=4
num2=6
i=min(4,6)
lcm=1
while i<=(num1*num2):
    if i%num1==0 and i%num2==0:
      lcm=i
      break
    i=i+1

print(lcm)
  






# cost 
# cpu register memory to usme hme iteration bchani hai




