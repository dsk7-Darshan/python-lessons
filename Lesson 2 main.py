# Variable = A container for value (string, integer,float,boolean)
#            A variable behaves as if it was the value it contains
# assign sign is "="  (equal) and then use "" or '' to write value in them

# 1. Strings
# These are the series of character that include symbol and number also like that email address.
# Example
first_name = "Dsk"
#to print this write it without quotes in print function
#if there use ive quotes then it print inside it that is first_name
print(first_name)
#for another things mix the use of these variables then use the f-string= formatted
# string literals for this use formate place the f or F before the quotes double or
# single then for showing that variable first_name or other use '{first_name}' this type writing.
#note if you missed the f or F placing then the output is not variable that we assigned get we
# get [I am {first_name}.] if place then correct output is [I am Dsk.]
print(f"I am {first_name}.")

# more examples
fruit = "Mango"
mail = "iam@123dmail.com"
print(f"I like {fruit}.")
print(f"My Email Address:{mail}.")

# Integers
# These numbers without decimal point
#the integer written without quotes due to they are integers
# Ex
#also below things can we define by integers
age = 25
quantity = 3
num_of_students = 30
print(f"I am {age} year old.")
print(f"I am Buying {quantity} Items ")
print(f"In My Class has {num_of_students} students.")

# if things are string then we place things in quotes

# Floats
# these are number that contain decimal point
# these also without quotes
#Ex
price = 100.98
cgpa_score = 9.1
distance_walk = 1.2
# this "_" is best use it give finding the assigns
# variable quickly, if we write variable using it
print(f"I Bought this thing in ${price}. ")
print(f"My cgpa score is {cgpa_score}.")
print(f"I walk {distance_walk} km everyday.")

# Boolean
# these are either true or false
# we write 1st letter capital  LIKE THIS - True or False
is_student = True

print(f"Yes,I am student? : {is_student}.")

# these boolean function not used directly it use with if like statements in programing
#Ex
#not require to put f-string due to no variable we place in below Ex
 # with this if then else used. if statement is 'false' then give the
 # value that place by else statement as below
 # and the between two condition of if-else comments placed and if-else write in the continue manner.
print("really?")
is_student1 = True
if is_student1:
    print("I am student.")
else:
    print("I am not student.")
print("This car for sell?")
is_car = False
if is_car:
    print("Yes, It is For Sell.")
else:
    print("Not for sell.")

is_online = True
if is_online:
    print("I am online.")
else:
    print("Error 404")

# extra I had written this for better view - print("really?")
# and print("This car for sell?")
