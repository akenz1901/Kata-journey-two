def get_list_of_numbers():
    list_of_number = [str(i) for i in range(1, 11)]

    questions = {dd: {} for dd in list_of_number}

    return questions


def get_file_elements():
    first_txt = open('nsc508s t1_22-1.txt', 'r')

    file_index = [lis.strip() for lis in first_txt]
    first_txt.close()

    return file_index


def analyze_question_answer():
    option_list = {'question': 'question', 'option1': 'option1', 'option2': 'option2', 'option3': 'option3',
                   'option4': 'option4', 'answer': 'answer'}
    content = get_file_elements()
    numbers = get_list_of_numbers()
    count = 0
    cou = 0

    for i in numbers:

        for item in option_list:
            option_list[item] = content[count]
            count += 1
        numbers[i] = option_list.copy()

    return numbers


print(analyze_question_answer())
# print(get_list_of_numbers())
