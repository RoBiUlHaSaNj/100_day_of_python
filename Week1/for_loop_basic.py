'''Python has two primitive loop commands:

while loops
for loops
'''


#for loop basic
# basic syntax

#c++   for(int i=0;i<n;i++)  start/condition/increment

#for variable in sequance :


# Over a list
fr =["app","ban","che"]
for i in fr:
    print(i)

alp =['a','b','c','d','e','f','g','h','i']
for i in alp:
    print(i)

#range()
for i in range(5):
     print(i)


for x in range(2, 6):
  print(x)
# start from 2  end 30 increment 3
for x in range(2, 30, 3):
  print(x)

#string loop
for letter in "Python":
    print(letter)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#The "inner loop" will be executed one time for each iteration of the "outer loop":
'''
app a
app b
app c
...... 
ban a
ban b
ban c
......
che a
che b
che c
.......
'''

#Nested Loops
alp =['a','b','c','d','e','f','g','h','i']
fr =["app","ban","che"]
for i in fr:
    for j in alp:
        print(i,j)



# break  The break statement exits the loop immediately.
for i in range(20):
    if i == 7:
        break
    print(i)
# Output : 0 1 2 3 4 5 6 7
# continue  The continue statement skips the rest of the code inside the
# loop for the current iteration and moves to the next iteration.
for i in range(5):
    if i == 2:
        continue
    print(i)
#output 0 1 3 4

# Nested Loops

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")





