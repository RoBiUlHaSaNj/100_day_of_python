#1 Age Classification:
age = 16

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

#2 Grading System:
grade = 85

if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You got an F.")


#3 Club Entry:
age = 20
has_ID = True
is_member = False

if (age >= 18 and has_ID) or is_member:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")
    
#leap year
print("Check if a Year is a leap year or not:")
num = int(input("Enter your Year: "))

if (num % 400 == 0) or (num % 100 != 0 and num % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")



#4 Multiple Conditions:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
x = 41

#nasted if else
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
