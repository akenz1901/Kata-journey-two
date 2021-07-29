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


def display_string(name, age):
    sentence_ = "my name is {0} i am {1} year old".format(name, age)
    return sentence_


def display_string_format_with_decimal(name, age, amount=0.0):
    sentence_ = "my name is {0} i am {1} year old i have %{2:f}".format(name, age, amount)
    return sentence_


def display_string_using_format_order():
    names = "michael", "ola", "akenz"
    print("They both bearing {2} and surname is {0} maybe the other one middle name is {1}".format(names[0], names[2],
                                                                                                   names[1]))


display_string_using_format_order()
