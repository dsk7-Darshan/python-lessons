# typecasting = The process of converting a value of one data type to
#               another (strings,integer,float,boolean)
#               Explicit vs Implicit
# How to check the type of function
name = "Dsk"
age = 25
cgpa = 9.1
student =True

# to check the type of function use "type(variable that we assumed)"
 # but to see output require the print function so we have to use format
 # "print(type(variable that want to we check))" imp thing no use quotes
# Ex
print(type(name))
print(type(age))
print(type(cgpa))
print(type(student))

# Explicit Ex
print("new values by changing type using Explicit Function format")
print("what function type of age?")
age = float(age)
# by this age is refined as flot
print(type(age))
# the change output is below
print(age)
#get output wih decimal point and
# remind write it without quotes due to it is variable
# my experiment use f-string and {} to make new statement print
print(f"My age is: {age} year old.")

# now convert float to integer
cgpa =int(cgpa)
print(cgpa)

# my experiment check how rounding of it is doing
# by taking examples
cgpa_1 = 9.5
cgpa_2 = 9.8
cgpa_3 = 9.3
cgpa_1 =int(cgpa_1)
cgpa_2 =int(cgpa_2)
cgpa_3 =int(cgpa_3)

print(cgpa_1)
print(cgpa_2)
print(cgpa_3)

# it is working as GIF that is greatest integer function that give
#   like if x inside it gives equal and less than value x+1 but always integer
# in simple way it means it remove decimal place and further everything after integer

# Ex2 Convert the boolean to string
print("Ex2 Convert the boolean to string:")
# in this example the converion done now showing true
# is not boolean it is string recheck by printing datatype
student =str(student)
print(student)
print(type(student))

# Ex2 Convert the string to boolean
print("Ex2 Convert the string to boolean:")
print("check for any positive - below is ans:")
age = bool(age)
print(age)

# if there is number rather than zero in age then it gives true
# if there is zero then give false
# ex for above
print("check for zero - below is ans:")
age1 = 0
age1 = bool(age1)
print(age1)
#also it on negative also true but on zero as above false
# let check for negative
print("let check for negative - below is ans: ")
age2 = -19999
age2 = bool(age2)
print(age2)

#ok now go forward

# also it happen if the string to boolean conversion if
# input string is anything rather than empty then get the answer as true even there is only space between quotes
print("input string is anything rather than empty then get the answer as true even there is only space between quotes:")
#Ex
print("Ex 1")
name1 = "xyz"
name1 = bool(name1)
print(name1)
#Ex
print("Ex 2")

name1_1 = " "
name1_1 = bool(name1_1)
print(name1_1)

# if it is empty without any space then only get answer as false
print("if it is empty without any space then only get answer as false:")
# Ex
name2 = ""
name2 = bool(name2)
print(name2)

#go forward

# in Explicit Function there is manually
# converting datatype from one from to another

# Implicit Function = in Explicit Function there is automatically
 # converting datatype from one from to another
#here we assign the variables
#Ex
print("Ex of Implicit function:")
x= 2
y= 2.0
x= x/y
print(x)
# you see the x is automatically defined as float rather than we assign it as integer by now it is float
print(type(x))
# it happening reason is operation of arithmatic expresion

# That's set Thank you.

