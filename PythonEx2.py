
#Exercise - 2

#1. Write a program to check whether a number is positive or negative.

num = float(input("Enter a Number : "))
if num>0:
    print("The number is Positive")
elif num<0:
    print("The number is negative")

else:
    print("The number is Zero")
#--------------------------------------------------------------------
    
#2.Write a program to check whether a number is even or odd.

num = int(input("Enter a Number : "))
if num%2==0:
    print("The number is Even")

else:
    print("The number is Odd")
    
#-------------------------------------------------------------------- 

#3.Write a program to check whether a person is eligible to vote (age ≥ 18)

num = int(input("Enter your Age : "))
if num>=18:
    print("You are Eligible to Vote")

else:
    print("You are not eligible to Vote")

#-------------------------------------------------------------------- 

#4.Write a program to check whether a given number is greater than 100.

num = int(input("Enter the Number : "))
if num>100:
    print("The given number is greater than 100")
elif num<100:
    print("The given number is lesser than 100")

else:
    print("The given number is 100")
    
#-------------------------------------------------------------------- 

#5.Write a program to check whether a character is a vowel or consonant

vowel = ['a', 'e', 'i', 'o', 'u' ]
char = input("Enter the Character (a to z):")
if (char in vowel):
    print("This Character is Vowels")

else:
    print("This Character is Consonant")

#-------------------------------------------------------------------- 
    
#6.Write a program to find the largest of two numbers.

num1 = int(input("Enter the Number 1 : "))
num2 = int(input("Enter the Number 2 : "))

if num1>num2:
    print(num1,"is the Largest Number")
    
elif num1<num2:
    print(num2,"is the Largest Number")

else:
    print("Both are same Numbers")
    
#-------------------------------------------------------------------- 

#7.Write a program to find the largest of three numbers.

num1 = int(input("Enter the Number 1 : "))
num2 = int(input("Enter the Number 2 : "))
num3 = int(input("Enter the Number 3 : "))
    
if num1>num2 and num1>num3:
   print(num1,"is the Largest Number")
    
elif num2>num1 and num2>num3:
   print(num2,"is the Largest Number")
    
elif num1==num2==num3:
   print("All are same Numbers")
    
else:
   print(num3,"is the Largest Number")
   
#--------------------------------------------------------------------


#8.Write a program to check whether a year is a leap year.

year = int(input("Enter a year: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')

'''
#-------------------------------------------------------------------- 
#9.Write a program to check whether a given character is uppercase, lowercase, digit, or special symbol.

char = input("Enter a single character: ")
if 'A' <= char <= 'Z':
    print(char,'is an uppercase character.')
elif 'a' <= char <= 'z':
    print(char,'is a lowercase character.')
elif '0' <= char <= '9':
    print(char,'is a digit.')
else:
    print(char,'is a special symbol.')

#-------------------------------------------------------------------- 

#10.Write a program to calculate grade based on marks:

mark = int(input('Enter your Mark:'))

if mark>=90 and mark<=100:
    print('PASS - Grade A')
elif mark>=75 and mark<=89:
    print("PASS - Grade B")
elif mark>=50 and mark<=74:
    print("PASS - Grade C")
else:
    print("FAIL")

#-------------------------------------------------------------------- 
#11.Write a program to create a simple calculator using conditional statements.

num1 = int(input("Enter the Number 1 :"))
num2 = int(input("Enter the Number 2 :"))
           
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = int(input("Select operation:"))

if operation == 1:
    op = num1 + num2
    print('The Addition Value is :',op)      

elif operation == 2:
    op = num1 - num2
    print('The Subtraction Value is :',op)

elif operation == 3:
    op = num1 * num2
    print('The Multiplication Value is :',op)

elif operation == 4:
    op = num1 / num2
    print('The Division Value is :',op)

else:
    print("Enter the Valid Operation")
    
#-------------------------------------------------------------------- 

#12.Write a program to check whether a triangle is valid using its sides.

side1 = int(input("Enter the Triangle side 1 :"))
side2 = int(input("Enter the Triangle side 2 :"))
side3 = int(input("Enter the Triangle side 3 :"))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("This is a Valid Triangle")
    
elif side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Please enter the valid traingle values")

else:
    print("This is not a valid Triangle")

#-------------------------------------------------------------------- 

#13.Write a program to classify a triangle as equilateral, isosceles, or scalene.

s1 = float(input("Length of side 1 :"))
s2 = float(input("Length of side 2 :"))
s3 = float(input("Length of side 3 :"))

if s1 == s2 == s3:
    print("This Triangle is Equilateral")
    
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("This Triangle is Isosceles")

elif s1+s2<= s3 or s1 + s3 <= s2 or s2 + s3 <= s1 or s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("This Triangle is Invalid")

else:
    print("This Triangle is Scalene")

#--------------------------------------------------------------------
    

#14.Write a program to calculate electricity bill based on units consumed.
           
print("RATE SLABS \n")
print("0-100 units: $2.00 per unit")
print("101-200 units: $3.00 per unit")
print("201-400 units: $4.00 per unit")
print("400+ units: $5.00 per unit\n")

units = float(input("Enter the total units consumed: "))

if units> 0:

    if units<=100:
        eb_amount=units*2
        print("Your total electricity bill is: Rs.",eb_amount)

    elif units>100 and units<=200:
        eb_amount=units*3
        print("Your total electricity bill is: Rs.",eb_amount)

    elif units>200 and units<=400:
        eb_amount=units*4
        print("Your total electricity bill is: Rs.",eb_amount)

    else:
        eb_amount=units*5
        print("Your total electricity bill is: Rs.",eb_amount)
else:
    print("Consumed units cannot be negative.")
    

#-------------------------------------------------------------------- 

#15.Write a program to check whether a number is a palindrome.

#-------------------------------------------------------------------- 

#16.Find the greatest of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(num,"is greatest number.")
elif num2 > num1:
    print(num2,"is greatest number.")
else:
    print("Both numbers are equal.")

#-------------------------------------------------------------------- 

#17.Check if a number is odd or even and positive or negative

num = int(input("Enter the number: "))

if num%2==0:
    print("This is Even number.")
    
else:
    print("This is Odd number.")

if num>0:
    print("This is Positive number.")
else:
    print("This is negative number.")

#-------------------------------------------------------------------- 

#19.input day pf week in number and print the day in String e.x. if user inputs 2 print "Monday" etc.

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

user_input = int(input("Enter the day of the week in number (1-7):"))

if user_input>0:

        if user_input==1:
            print("The day for number is :",days[0])
        elif user_input==2:
            print("The day for number is :",days[1])
        elif user_input==3:
            print("The day for number is :",days[2])
        elif user_input==4:
            print("The day for number is :",days[3])
        elif user_input==5:
            print("The day for number is :",days[4])
        elif user_input==6:
            print("The day for number is :",days[5])
        elif user_input==7:
            print("The day for number is :",days[6])
        elif user_input>7:
            print("Invalid input. Please enter a (1-7) number ")

else:
    print("Invalid input. Please enter a whole number ")

#-------------------------------------------------------------------- 

#20.Input day of month in number and print the name of the month  in String e.x. if user inputs 4 print "April" etc.

days = ["January","Febrary","March","April","May","June","July","August","September","October","November","December"]

user_input = int(input("Enter the month in number (1-12):"))

if user_input>0:

        if user_input==1:
            print("The month for this number is :",days[0])
        elif user_input==2:
            print("The month for this number is :",days[1])
        elif user_input==3:
            print("The month for this number is :",days[2])
        elif user_input==4:
            print("The month for this number is :",days[3])
        elif user_input==5:
            print("The month for this number is :",days[4])
        elif user_input==6:
            print("The month for this number is :",days[5])
        elif user_input==7:
            print("The month for this number is :",days[6])
        elif user_input==8:
            print("The month for this number is :",days[7])
        elif user_input==9:
            print("The month for this number is :",days[8])
        elif user_input==10:
            print("The month for this number is :",days[9])
        elif user_input==11:
            print("The month for this number is :",days[10])
        elif user_input==12:
            print("The month for this number is :",days[11])
        elif user_input>12:
            print("Invalid input. Please enter a (1-12) number ")

else:
    print("Invalid input. Please enter a whole number ")

#--------------------------------------------------------------------

#21.program to find sum of all even numbers between 1 to n.

num = int(input("Enter the number :"))
total_sum = 0
    # Start loop from 2 (first even number) and increment by 2
    
for num in range(2, num + 1, 2):
        total_sum += num
print("Sum of all even numbers between 1 to",num+1, 'is :', total_sum)


#--------------------------------------------------------------------  

#22.Python program to count the total number of digits in a number.

num = input("Enter the numbers : ")
count = 0
for digit in num:
    count += 1
print("The number is:",num)
print("The total number of digits in the number is:",count)


#-------------------------------------------------------------------- 

#23.Python program to find the factorial of a number

n = int(input("Enter the number: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is: 1")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("The factorial value is:", fact)
        
#--------------------------------------------------------------------

#24.Input 2 numbers and find the power of one number to another

base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent number: "))

result = base ** exponent

print(base,"raised to the power of",exponent,"is",result)

#-------------------------------------------------------------------- 









                 
                 













