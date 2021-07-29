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


def eliminate_punctuation(sentence):
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    new_sentence = ""

    for char in sentence:
        if char not in punctuations:
            new_sentence += char
    return new_sentence


sentence = """Pythons are constrictors, which means that they will 'squeeze' the life
                           out of their prey. They coil themselves around their prey and with
                           each breath the creature takes the snake will squeeze a little tighter
                           until they stop breathing completely. Once the heart stops the prey
                           is swallowed whole. The entire animal is digested in the snake's
                           stomach except for fur or feathers. What do you think happens to the fur,
                           feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
                           you guessed it --- snake POOP! """
result = eliminate_punctuation(sentence).split(sentence)
print(result)
