# sentence = "My name Akinsanya Michael"
# print(sentence[:])


def find(words, char):
    counter = 0
    for i in words:

        if i == char:
            return counter
        counter += 1
    return -1


def count_occurrence_of_character(word, char):
    counter = 0
    for i in word:
        if i == char:
            counter += 1
    return counter


def split(sentence):
    new_sentence = sentence.split()
    return new_sentence


def eliminate_punctuation():
    punctuations = "!@#$%^&*()_-|\><'.;:"
    
