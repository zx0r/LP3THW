from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copy data from the file {from_file} to file {to_file}")
#can you put the following two lines of code into one?

in_file = open(from_file)
indata = in_file.read()

print(f"Source file is {len(indata) } bytes")
print(f"Does target file exist? {exists(to_file) }")
print("Ready, press the key Enter to continue or CTRL+C to cancel.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Great, it's all done!")

out_file.close()
in_file.close()

