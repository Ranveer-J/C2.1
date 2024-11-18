name = "penguin"
age = 15
is_student = True
weight = 38.5

print("Name is :" , name)
print("Variable type is :", type(name) )
print("Age is :" , age)
print("Variable type is :", type(age) )
print(" Student is :" , is_student)
print("Variable type is :", type(is_student) )
print("Weight is :" , weight)
print("Variable type is :", type(weight) )

print("After Type casting...")

age =  str(age)
print("The new variable type is", type(age))
name =  str(name)
print("The new variable type is",type(name) )
is_student =  str(is_student)
print("The new variable type is", type(is_student))
weight =  str(weight)
print("The new variable type is", type(weight))





num1 = 76
num2 = 24

print("The sum of num1 and num2 is", num1 + num2)
print("The difference between num1 and num2 is", num1 - num2)
print("The numbers are equal?", num1==num2)
print("num1 is greater that num2?" ,num1 > num2)

result = num1/2+num2**2+10
print(result)

firstname = "Ranveer"
lastname = "Jaiswal"
fullname = (firstname + lastname)
print(fullname)

print(fullname[0])

user_name = input("what is your name?")
print(user_name)