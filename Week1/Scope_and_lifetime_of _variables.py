'''1. Scope of Variables

  1.Local Scope: Variables defined within a function are in the local scope. 
They can only be accessed within that function.'''



def my_function():
    local_var = 10  # Local scope
    print(local_var)

my_function()  # Output: 10
# print(local_var)  # Error: NameError, as local_var is not accessible here.


 ''' 2.Global Scope: Variables defined at the top level of a script or module are in the global scope. 
They can be accessed anywhere in the module.'''

global_var = 20  # Global scope

def another_function():
    print(global_var)  # Accessible within the function

another_function()  # Output: 20

'''   3.Enclosing Scope: This applies to nested functions. If a function is defined inside another function, 
it can access variables from the enclosing function’s scope.'''


  def outer_function():
    outer_var = 30  # Enclosing scope

    def inner_function():
        print(outer_var)  # Accessible within the nested function

    inner_function()  # Output: 30

outer_function()




'''2. Lifetime of Variables


     1.Local Variables: Local variables exist only as long as the function in which they are defined is executing.
Once the function exits, the local variables are destroyed.'''

def my_function():
    temp_var = 40  # Local variable
    print(temp_var)

my_function()  # Output: 40
# After this point, temp_var no longer exists.


'''    2.Global Variables: Global variables exist for the duration of the program. 
They are created when the program starts and are destroyed when the program ends.'''


global_var = 50  # Global variable

def my_function():
    print(global_var)

my_function()  # Output: 50
# global_var exists as long as the program runs




  '''  3.Modifying Global Variables

To modify a global variable inside a function, you need to use the global keyword.'''


counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Output: 1











