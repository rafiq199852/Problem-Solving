#!/usr/bin/env python
# coding: utf-8

# #### Write a Python program which accepts the radius of a circle from the user and compute the area.
# ###### Program Console Sample Output 1:
# ###### Input Radius: 0.5
# ###### Area of Circle with radius 0.5 is 0.7853981634

# In[6]:


import math
radius = float(input("Enter Radius of circle:"))
area = math.pi*radius**2
print("Area of Circle with radius ",radius,"is ","%.10f"%area)


# ## 2. Check Number either positive, negative or zero

# #### Write a Python program to check if a number is positive, negative or zero
# ###### Program Console Sample Output 1:
# ###### Enter Number: -1
# ##### Negative Number Entered
# ###### Program Console Sample Output 2:
# ##### Integer: 3
# ##### Positive Number Entered
# ###### Program Console Sample Output 3:
# ##### Integer: 0
# ###### Zero Entered

# In[5]:


number = int(input("Enter Number: "))
if number>0:
    print("Positive Number Entered")
elif number<0:
     print("Negative Number Entered")
else:
    print("Zero Entered")


# In[32]:


number = int(input("Enter Number: "))
if number>0:
    print("Positive Number Entered")
elif number<0:
     print("Negative Number Entered")
else:
    print("Zero Entered")


# In[35]:


number = int(input("Enter Number: "))
if number>0:
    print("Positive Number Entered")
elif number<0:
     print("Negative Number Entered")
else:
    print("Zero Entered")


# ## 3. Divisibility Check of two numbers

# #### Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# ##### Program Console Sample Output 1:
# ###### Enter numerator: 4
# ###### Enter Denominator: 2
# ##### Number 4 is Completely divisible by 2
# ###### Program Console Sample Output 2:
# ##### Enter numerator: 7
# 
# ##### Enter Denominator: 4
# ###### Number 7 is not Completely divisible by 4

# In[9]:


numerator = int(input("Enter Numerator: "))
denominator = int(input("Enter Denominator: "))
if numerator%denominator==0:
    print("Number ",numerator,"is Completely divisible by ",denominator)
else:
        print("Number",numerator,"is not Completely divisible by",denominator)


# In[10]:


numerator = int(input("Enter Numerator: "))
denominator = int(input("Enter Denominator: "))
if numerator%denominator==0:
    print("Number ",numerator,"is Completely divisible by ",denominator)
else:
        print("Number",numerator,"is not Completely divisible by",denominator)


# ## 4. Calculate Volume of a sphere

# ##### Write a Python program to get the volume of a sphere, please take the radius as input from user

# ##### Program Console Output:
# ##### Enter Radius of Sphere: 1
# ###### Volume of the Sphere with Radius 1 is 4.18

# In[6]:


import math
radius = int(input("Enter Radius of Sphere: "))
answer = (4/3)*math.pi*(radius)**3
print("Volume of the Sphere with Radius",radius,"is","%.2f"%answer)


# ## 5. Copy string n times
# #### Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# ##### Program Console Output:
# ##### Enter String: Hi
# ###### How many copies of String you need: 4
# ###### 4 Copies of Hi are HiHiHiHi

# In[15]:


n=input("Enter String:")
num=int(input("How many copies of String you need:"))
for i in range(0,num):
    print(n,end='')  


# # 6. Check if number is Even or Odd
# ### Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
# #### Program Console Output 1:
# ##### Enter Number: 4
# ###### 4 is Even
# #### Program Console Output 2:
# ##### Enter Number: 9
# ###### 9 is Odd

# In[36]:


number = int(input("enter number: "))

if (number % 2) == 0:
    print(number , "is even")
else:
    print(number , "is odd")


# In[37]:


number = int(input("enter number: "))

if (number % 2) == 0:
    print(number , "is even")
else:
    print(number , "is odd")


# ## 7. Vowel Tester
# ### Write a Python program to test whether a passed letter is a vowel or not
# #### Program Console Output 1:
# ##### Enter a character: A
# ###### Letter A is Vowel
# #### Program Console Output 2:
# ##### Enter a character: e
# ###### Letter e is Vowel
# #### Program Console Output 2:
# ##### Enter a character: N
# ###### Letter N is not Vowel

# In[30]:


character = input("Enter a character:")
if character in "aeiouAEIOU":
        print("Letter",character,"is Vowel")
else:
        print("Letter",character,"is not Vowel")


# ## 8. Triangle area
# ### Write a Python program that will accept the base and height of a triangle and compute the area
# ###### Reference:
# https://www.mathgoodies.com/lessons/vol1/area_triangle

# In[31]:


'''Area of Triangle'''
base = int(input("Enter the base of triangle:"))
height = int(input("Enter the height of triangle:"))
area = (base*height)/2
print("The area of triangle is:",area)


# ## 9. Calculate Interest
# ### Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# #### Program Console Sample 1:
# ##### Please enter principal amount: 10000
# ###### Please Enter Rate of interest in %: 0.1
# ###### Enter number of years for investment: 5
# ###### After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1

# In[41]:


num = int(input("Please Enter principal amount:"))
rate_of_interest = float(input("Please Enter Rate of intereist in %:"))
investment_years = int(input("Enter number of years for investment: "))
print ("after", investment_years , "years your principal amount" , num,
       "over an interest rate of" , rate_of_interest , " % will be " , round((num*(1+rate_of_interest)**investment_years),1))


# ## 10. Euclidean distance
# ### write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# #### Program Console Sample 1:
# ###### Enter Co-ordinate for x1: 2
# ###### Enter Co-ordinate for x2: 4
# ###### Enter Co-ordinate for y1: 4
# ###### Enter Co-ordinate for y2: 4
# ###### Distance between points (2, 4) and (4, 4) is 2

# ###### Reference:
# https://en.wikipedia.org/wiki/Euclidean_distance

# In[45]:


import math
x1= int(input("Enter Co-ordinate for x1:"))
x2= int(input("Enter Co-ordinate for x2:"))
y1= int(input("Enter Co-ordinate for y1:"))
y2= int(input("Enter Co-ordinate for y2:"))
answer = math.sqrt((y1-x1)**2+(y2-x2)**2)
print("Distance between points (",x1,",",x2,")","and (",y1,",",y2,") is",answer)


# ## 11. Feet to Centimeter Converter
# ### Write a Python program to convert height in feet to centimetres.
# ##### Program Console Sample 1:
# ###### Enter Height in Feet: 5
# ###### There are 152.4 Cm in 5 ft
# ###### Reference:
# https://www.rapidtables.com/convert/length/feet-to-cm.html

# In[48]:


feet = int(input("Enter Height in Feet:"))
cm = feet*12*2.54
print("There are",cm,"Cm in",feet,"ft")


# ## 12. BMI Calculator
# ### Write a Python program to calculate body mass index
# ##### Program Console Sample 1:
# ###### Enter Height in Cm: 180
# ###### Enter Weight in Kg: 75
# ###### Your BMI is 23.15

# In[55]:


height = int(input("Enter Height in Cm:"))
height_m = height/100
weight = int(input("Enter Weight in Kg:"))
BMI = weight/math.pow(height_m,2)
print("Your BMI is",round(BMI,2))


# ## 13. Sum of n Positive Integers
# ### Write a python program to sum of the first n positive integers
# #### Program Console Sample 1:
# ###### Enter value of n: 5
# ###### Sum of n Positive integers till 5 is 15

# In[67]:


n=int(input("Enter value of n:"))
a=0
for i in range(0,n+1):
    a=a+i
print("Sum of n Positive integers till",n,"is",a)


# ## 14. Digits Sum of a Number
# ### Write a Python program to calculate the sum of the digits in an integer
# #### Program Console Sample 1:
# ##### Enter a number: 15
# ###### Sum of 1 + 5 is 6
# #### Program Console Sample 2:
# ##### Enter a number: 1234
# ###### Sum of 1 + 2 + 3 + 4 is 10

# In[87]:


number = input("enter a number: ")
sum = 0
counter = 1
print("sum of", end="")
for i in number:
    if len(number) > counter:
        sum = sum + int(i)
        print("" , i , "+" , end="")
        counter +=1
    else:
        sum = sum + int(i)
        print("" , i , end="")
        counter +=1 
print(" is",sum)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




