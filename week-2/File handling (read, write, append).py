# 1. Opening Files
# Use the open() function to open a file. It returns a file object and takes two main arguments: the filename and the mode.
file = open("example.txt", mode="r")  # 'r' for reading

# Modes:
# 'r': Read (default mode) - Opens the file for reading.
# 'w': Write - Opens the file for writing (creates a new file if it doesn’t exist, or truncates the file if it exists).
# 'a': Append - Opens the file for appending data to the end.
# 'b': Binary mode - Used with other modes for binary files (e.g., 'rb', 'wb', 'ab').
# 'x': Exclusive creation - Creates a new file and fails if the file already exists.

# 2. Reading Files
# read(): Reads the entire file content.
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# readline(): Reads one line at a time.
file = open("example.txt", "r")
line = file.readline()
while line:
    print(line, end="")  # The end="" prevents adding extra new lines
    line = file.readline()
file.close()

# readlines(): Reads all lines and returns a list.
file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()

# 3. Writing Files
# write(): Writes a string to the file.
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a new file.\n")
file.close()

# writelines(): Writes a list of strings to the file.
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open("example.txt", "w")
file.writelines(lines)
file.close()

# 4. Appending to Files
# 'a' mode: Opens a file for appending.
file = open("example.txt", "a")
file.write("Appending a new line.\n")
file.close()

# 5. Using with Statement
# The with statement automatically handles closing the file, even if an error occurs. This is a best practice for file handling.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# The file is automatically closed after the with block is exited.

# 6. Binary Files
# Handling binary files is similar to text files, but you need to use the 'b' mode.

# Reading a binary file
with open("example.jpg", "rb") as file:
    content = file.read()

# Writing a binary file
with open("example_copy.jpg", "wb") as file:
    file.write(content)

# 7. File Operations
# file.seek(offset, whence): Move the file cursor to a specific position.
# offset: Number of bytes to move the cursor.
# whence: Starting point (0=start, 1=current position, 2=end).

file = open("example.txt", "r")
file.seek(5)  # Move cursor to the 5th byte
content = file.read()
print(content)
file.close()

# file.tell(): Returns the current position of the file cursor.
file = open("example.txt", "r")
print(file.tell())  # Output: 0 (beginning of the file)
file.read(5)
print(file.tell())  # Output: 5 (cursor is at the 5th byte)
file.close()

# 8. Practical Examples
# Copying Content from One File to Another
with open("source.txt", "r") as source_file:
    content = source_file.read()
with open("destination.txt", "w") as destination_file:
    destination_file.write(content)

# Counting Words in a File
with open("example.txt", "r") as file:
    content = file.read()
    words = content.split()
    print(f"Number of words: {len(words)}")
