# loop-->repetion /iteration
# intro to loops


# infinte loop
# i=1
# while i<5:
#     print(i)
#     print('hello')


# i=2
# while(i>=4):
#     print(i)
#     print('hello')


# 1,2 ,3,4,5,6,7,,8,9,10
# 2,4,6,8,10
# 1,2 ,3,4,5,6,7,,8,9,10

# sum=0
# i=0
# cnt=1
# while i<10:
#     sum=sum+cnt
#     cnt=cnt+1
#     i=i+1

# print(sum)

# 7450


# n=987654
# cnt=0
# while n>0:
#     n=n//10
#     cnt=cnt+1

# print(cnt)


# 123-->1+2+3=6

# n=1234
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+rem
#     n=n//10

# print(sum)

# 321---123
# 1ones digit-->100 digit
# n>0 n=n//10
# rem=n%10

n=123
rev=0
while n>0:
      rem=n%10
      rev=rev*10+rem
      print(rev)
      n=n//10


