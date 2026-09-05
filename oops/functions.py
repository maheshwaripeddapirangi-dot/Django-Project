# 1. Arbitrary Arguments (*args, **kwargs)

# Write a function that takes any number of item prices and optional customer details, 
# then prints the total and details.

def checkout(*prices,**info):
    total=sum(prices)
    print("Total:",total)

    for key,value in info.items():
        print(f"{key}:{value}")
checkout(100,200,50,name="Alex",payment="Card")

# Write a function that accepts any number of numbers (for example: 
# marks of a student in different subjects) and prints their average.

def avg_marks(*marks,**sub):
    avg=sum(marks)/len(marks)
    
    print("Student average marks:",avg)
    

    for (key,value),mark in zip(sub.items(),marks):
            print(f"{key}:{value}-->{mark}")
avg_marks(98,86,89,99,95,99,sub1="Telugu",sub2="Hindi",sub3="English",sub4="Maths",sub5="Science",sub6="Social")


# Create a function that takes multiple subjects (*args) and 
# student details (**kwargs) such as name, age, grade, and section, and prints them.

def student(*sub,**stu_details):
     print("Subjects:",sub)
     for key,value in stu_details.items():
          print(f"{key}:{value}")
student("Telugu","Hindi","English","Mathematics","Science","Social",Name="Maheshwari",Age=21,Grade="A+",Section="E/M")

# Build a function that accepts product names (*args) and optional metadata (**kwargs) like category, brand, price range, or availability.

def Company(*products,**data):
     print("Products:")
     for product in products:
          print(product)
     print("Mata data")     
     for key,value in data.items():
          print(f"{key}:{value}")
Company("Laptop","Mobile","Tab","Computer",category="Electronics",brand="HP",price=100000,availability="Ready to deliver")

# 2. Pure Functions

# Write a pure function that takes a list of numbers and returns a new list with each number doubled.

def double_list(numbers):
     return[n*2 for n in numbers]
print("double of given list: ",double_list([1,2,3]))

# Write a pure function to convert a list of temperatures (for example: daily temperatures) from Celsius to Fahrenheit.

def celsius_to_fahrenheit(celcius):
     return(celcius*9/5)+32
print("celsius_to_fahrenheit: ",celsius_to_fahrenheit(25))


# Create a function that returns the cube of each number in a list (for example: a list of input values provided by the user).

def cube_list(num):
     return[n**3 for n in num]
print("Cube of given list: ",cube_list([1,2,3,4,5,6,7,8,9,10]))


# taking input from user

def cube_num(number):
     return[num**3 for num in number]
n=int(input("Enter number of elements: "))
number=[]
for i in range(n):
     num=int(input(f"Enter number {i+1} "))
     number.append(num)
result=cube_num(number)
print("Original List:",number)
print("Cube list:",result)
     
# Write a function that takes a number (for example: user input) and returns whether it is even or odd.

def even_odd(num):
     return["Even" if n%2==0 else "Odd" for n in num]
print(even_odd([35,62,78,88,97,54]))


# input from user

def even_odd(num):
     return["Even" if n%2==0 else "Odd" for n in num]
n=int(input("Number of elements for even and odd "))
num=[]
for i in range(n):
     a=int(input("Enter "))
     num.append(a)
print(even_odd(num))


# 3. Returning Multiple Values

# Write a function that takes a list of numbers and returns the minimum and maximum values.

def get_min_max(numbers):
     return min(numbers),max(numbers)
low,high=get_min_max([4,2,9,1])
print(f"low value is {low},\nhigh value is {high}")


# Write a function that returns the sum and average of a list of numbers (for example: marks obtained in different subjects).

def sum_avg(marks):
     avg=sum(marks)/len(marks)
     return sum(marks),avg
sum,avg=sum_avg([98,96,84,95,90,99])
print(f"sum of marks={sum}\n Average of marks={avg}")


# Create a function that takes two numbers (dividend and divisor) and returns their quotient and remainder.

def Coeff_remainder(n1,n2):
     coefficient=n1//n2
     remainder=n1%n2
     return coefficient,remainder
coefficient,remainder=Coeff_remainder(106,10)
print(f"Cofficient is {coefficient}\nRemainder is {remainder}")

# Write a function that returns both the square and cube of a number (for example: a number entered by the user).

def square_cube(num):
     square=num**2
     cube=num**3
     return square,cube
n=int(input("Enter number for square and cube: "))
square,cube=square_cube(n)
print(f"Sqare of {n} is {square}\nCube of {n} is {cube}")

# 4. Recursive Functions

# Write a recursive function to calculate factorial.

def factorial(num):
     if num==0:
          return 1
     return num*factorial(num-1)
print(f"factorial of 5 is {factorial(5)}")


# Write a recursive function to calculate the sum of numbers from 1 to n (where n is a positive integer provided by the user).

def sum_num(num):
     if num<0:
          return "Enter Positive Integer only"
     sum=0
     for i in range(num+1):
          sum+=i
     return sum
n=int(input("Enter number for sum"))
print(sum_num(n))


# Create a recursive function to print numbers from n to 1 (where n is a positive integer).

def print_num(num):
     if num<0:
         return "Enter Positive Integer only"
     for i in range(num,0,-1):
          print(i)
n=int(input("Enter number for printing ")) 
print_num(n)


# Write a recursive function to calculate the power of a number (x^n), where x is the base and n is a non-negative integer exponent.

def power(n,x):
     if n<0:
          return "non-negative integer exponent."
     return x**n
n=int(input("Enter exponent "))
x=int(input("Enter base "))
print(f"Power of {x}^{n} is {power(n,x)}")
