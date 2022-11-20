import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "A class is created with the name %%%, wich inherits from %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% combines __init__ with parametrs self and parametrs ***.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% combines a function named *** with parametrs self and @@@,",
    "***.***(@@@)":
    "Created *** as an instance of class %%%.",
    "***.***(@@@)":
    "Function *** is obtained from ***, and then called with parametrs self, @@@.",
    "***.*** = '***'":
    "The atribute *** is obtained from *** and then set to '***'."
}

#Phrase memorization training
if len(sys.argv) == 2 and sys.argv[1] == "russian":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#Loading words from the server
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
        random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fictious class name
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fictious other name
        for word in other_names:
            result = result.replace("***", word, 1)
    
        #list of fictious parametrs
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

#Execute until CTRL+Z is pressed
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")
