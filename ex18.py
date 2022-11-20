#similar to argv scripts
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: (arg1), arg2: (arg2)")

#ok, here instead of *args we do the following
def print_two_again(arg1, arg2):
    print(f"arg1: (arg1), arg2: (arg2)")

#takes only one argument
def print_one(arg1):
    print(f"arg1: (arg1)")

#takes no arguments
def print_none():
    print("And I don't get anything.")

print_two("Data","Science")
print_two_again("Data","Science")
print_one("The best!")
print_none()
