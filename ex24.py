print("Let's practice!")
print('You should know about \\ escape sequences that:')
print('\n control line breaks and \t indentation.')

poem = """
\t For happiness I need very little.
   I want you \n I gently hug.
   I always want
   I'm next to you
   \n\t\t and never let go
"""

print("--------------------------------------------")
print(poem)
print("--------------------------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be live: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)

#remember this is another way to format a string
print("Beginning with: {}".format(start_point))
#same as with string f""
print(f"We have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can also do it this way:")
 
formula = secret_formula(start_point)

#an easy way to apply a list to a string being formatted
print("We have {} beans, {} jars and {} boxes.".format(*formula))

      

