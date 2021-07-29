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


def split(sentence_):
    new_sentence = sentence_.split()
    return new_sentence


def eliminate_punctuation(sentence_):
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    new_sentence = ""

    for char in sentence_:
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
    outputs = "3**2 = {0}, 2 + 2 = {1} three decimal number = {2:.3f}".format(3 ** 2, 2 + 2, 3.1414504444)
    print(outputs)

    outputs = "||{0:<15}||{1:^15}||{2:>15}||"
    print(outputs.format(names[0], names[1], names[2]))

    outputs = "Using x to format {0} to hexadecimal {0:x}"
    print(outputs.format(123345))

    outputs = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
    print(outputs.format('i', '2**2', '3**2', '5**2', '10**2', '20**2'))

    for i in range(1, 11):
        print(outputs.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))


display_string_using_format_order()
