1. and
x = True
y = False
result = x and y  # False because y is False

2. or

x = True
y = False
result = x or y  # True because x is True

3. not
x = True
result = not x  # False because x is True


4. Combining Logical Operators
x = 5
y = 10

# Check if x is greater than 0 and y is less than 20
result = (x > 0) and (y < 20)  # True

# Check if x is less than 0 or y is greater than 5
result = (x < 0) or (y > 5)   # True

5. Short-Circuit Evaluation

def func1():
    print("func1 called")
    return False

def func2():
    print("func2 called")
    return True

result = func1() and func2()  # func2 is not called because func1() is False

Comparison with Other Operators
x = 10
y = 20

# Check if x is between 5 and 15
result = (x > 5) and (x < 15)  # True

# Check if y is either less than 10 or greater than 15
result = (y < 10) or (y > 15)  # True
