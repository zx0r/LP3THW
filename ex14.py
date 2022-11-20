from sys import argv
script, user_name = argv
prompt = '> '

print(f"Hi, {user_name}, I'm {script}.")
print("I want to ask you some questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What your computer do you work on?")
computer = input(prompt)

print(f"""
    So you answered {likes} to the question wheter you like me.
    You live {lives}.I can't imagine where it is.
     And you have a computer {computer}.
     Wonderful) 
      """)

