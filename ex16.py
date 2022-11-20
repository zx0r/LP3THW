from sys import argv

script, filename = argv

print(f"I'm about to delete the file {filename}.")
print("If you don't want to erase it, press CTRL+C (^C).")
print("if you want to delete the file, press the Enter key.")

input("?")

print("Opening a file...")
target = open(filename, 'w')

print("File Cleaning.GoodBye!")
target.truncate()

print("Now I ask you three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I will write this to a file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, I will close the file.")
target.close()
