# area and volume calculator

#length = input("Enter The length:")
#length =float(length)
#width = input("Enter The width:")
#width = float(width)

# instead of above we dierectly do this with the float use directly in 1st like below
print("*********************************************")
print("area and volume calculator")
# As below the thing are going for modification I added the below things
print("*********************************************")
print("for area of 2D rectangle and square")
length = float(input("Enter The length:"))
width = float(input("Enter The width:"))
area = length * width
print("*********************************************")
print(f"The Area is : {area}cm^2.")
print("*********************************************")


# for 3d rectangle we can add the height
print("for 3D rectangle, The volume is -`")
print("*********************************************")
length = float(input("Enter The length:"))
width = float(input("Enter The width:"))
height = float(input("Enter The height:"))
Volume = length * width * height
print("*********************************************")
print(f"The Volume is : {Volume}cm^3.")
print("*********************************************")


# for Area of circle
print("fro Area of Circle-")
print("*********************************************")

radius = float(input("Enter The radius:"))

area = radius * radius * 3.14
print("*********************************************")
print(f"The Volume is : {area}cm^2.")

print("*********************************************")
print("Thank You.....................................")
print("*********************************************")

# we can add more things we can modify it by make ing selector type 1]option choose the shape 2]give parameter to get output
