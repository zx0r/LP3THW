from sys import argv

script, filename = argv

txt = open(filename)

print(f"File contents {filename}:")
print(txt.read())

print("Enter the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
