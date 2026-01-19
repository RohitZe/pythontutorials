# problems to solve
# 1.Student Grade Calculator
# Take marks of a student (0–100) and print the grade.
# Conditions
# >= 90 → Grade A
# >= 75 and < 90 → Grade B
# >= 60 and < 75 → Grade C
# < 60 → Fail


# if condtion:
#     //
# elif conditon
#    //
# elif conditon
#   //
# else
#     //

# 2.Electricity Bill Calculator
# Units consumed:
# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Above 200 units → ₹10/unit
# Take units as input and print the total bill.




# num1=int(input('enter the first number? '))
# num2=int(input('enter the second number? '))

# op=input('enter the operation: ')

# if op=='+':
#     print(num1+num2)

#nested if
#if ke andar if

# else:
#     if num2==0:
#         print('it is infinte condition')


# 3.Simple Calculator 
# Take:
# two numbers
# an operator (+, -, *, /)
# Perform the operation.
#Edge case: Handle division by zero using if


# 4.Atm Withdrawl Problem
# Take:
# account balance
# withdrawal amount
# Conditions:
# Amount must be multiple of 100
# Amount ≤ balance
# Minimum balance after withdrawal should be ₹500
# Print Success or Failure message.



# 5. Final challenge
# Take product price
# If price > 5000 → 20% discount
# If price > 3000 → 10% discount
# Else → No discount
# Print final price using round()

#price will be input by user float
#calculate discount for values greater than 5000
#calculate discount for values greater 3000 
#print

price=float(input('Enter the price? '))
bigDiscount=(20/100)*price
smallDiscount=(10/100)*price
if price>=5000:
    print('you need to pay',(price-bigDiscount))
elif price>=3000 and price<5000:
    print('you need to pay',(price-smallDiscount))


#temperature converter
#celsius farheit
#bmi calculator
