'''Python has two primitive loop commands:

while loops
for loops'''



# basic syntax

#c++  initialization   while(condition){  ......... increment)
''' int i =0;
while(i<=n)
{
// 
//
i++;
}

'''

# same as  c++  initialization  while condition :

#basic
count = 0
while count < 5:
    print(count)
    count += 1
# Output :0 1 2 3 4 5


# break  The break statement exits the loop immediately.
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# Output : 0 1 2 3 4 5 6 7
# continue  The continue statement skips the rest of the code inside the
# loop for the current iteration and moves to the next iteration.


i = 0
while i < 5:
    if i == 4:
        i += 1
        continue  # Skip the rest of the loop when i == 4

    print(i)
    i += 1  # Increment i

#output 0 1 3 4

# Nested Loops

i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1



