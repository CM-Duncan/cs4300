"Caroline Duncan, 2/13/26, opens a file, reads its contents, and returns the total number of words in it. "
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)
