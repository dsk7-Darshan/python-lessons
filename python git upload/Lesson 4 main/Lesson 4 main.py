#use of input function
#for user input we use the input function by console it take the input

# Ex1
## input("Enter Your Name:")
# for above i place the hashtag due to it not require below for test remove that hashtag and run the code

# here require the quotes to take input
# by only this not show anything also we have to store the input anywhere
# so we use for that store we have to assign it as variable as
# something as we are doing in previous lesson do
# As Below
name = input("Enter Your Name:")
print(f"My name is {name}.")

# Next
age= input("Entre Your age:")
print(f"My age is {age} year old.")

#now the input are like strings that we assigned the quotes
# for we get the age plus one or any by increasing or decreasing then require to convert age to reassigning it as integer
print("by require 1plus age :")
age = int(age)
age = age +1
print(f"My age is {age} year old.")
# here happen the function work one by one work the by above output as input below function give about put then as below we get 25year old age
print("by require 1differ age :")
age = int(age)
age = age -1
print(f"My age is {age} year old.")
#to solve this we have to differ by 1 due to above already 1 differed so below is answer
print("by require 1differ age and by the correcting above age require age:")
age = int(age)
age = age -1
print(f"My age is {age} year old.")

# the use of before lesson typecasting here to change string to integer
# also we here we convert the string in to float for more correct

print("my exact age :") # with the float
age = float(age)
age = age +1
print(f"My age is {age} year old.")