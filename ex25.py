def break_words(stuff):
    """This function parses text into words."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort words."""
    return sorted(words)

def print_fist_word(words):
    """Displays the first word after extraction."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Displays the last word after extraction."""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """Takes a whole sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Displays the first and the last words of a sentence."""
    words = break_words(sentence)
    print_fist_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts words and then outputs first and last."""
    words = sort_sentence(sentence)
    print_fist_word(words)
    print_last_word(words)
    
