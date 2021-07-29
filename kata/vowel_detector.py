def confirm_vowels(message):
    message.lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    empty_container = []
    for i in message:
        if i not in vowel:
            empty_container.append(i)
    return empty_container


def remove_vowel(sentence):
    """This function returns a new String"""
    new_sentence = ""
    vowels = "aeiouAEIOU"
    for letter in sentence:
        if letter not in vowels:
            new_sentence += letter
    return new_sentence

