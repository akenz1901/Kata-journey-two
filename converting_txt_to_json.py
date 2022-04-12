import json


def get_list_of_numbers(num: int):
    list_of_number = [str(i) for i in range(1, num+1)]

    questions = {dd: {} for dd in list_of_number}

    return questions


def get_file_elements():
    first_txt = open('BUS105.txt', 'r')

    file_index = [lis.strip() for lis in first_txt]
    first_txt.close()

    return file_index


def analyze_question_answer():
    option_list = {'question': 'question', 'option1': 'option1', 'option2': 'option2', 'option3': 'option3',
                   'option4': 'option4', 'answer': 'answer'}
    content = get_file_elements()
    numbers = get_list_of_numbers(70)
    count = 0

    for i in numbers:

        for item in option_list:
            option_list[item] = content[count]
            count += 1
        numbers[i] = option_list.copy()

    return numbers


def convert_output_to_json(file_name=''):
    arrange_dict = analyze_question_answer()
    json_file_name = file_name + '.json'

    file = open(json_file_name, 'w')
    json.dump(arrange_dict, file, indent=4, sort_keys=False)
    file.close()


# print(get_file_elements())
convert_output_to_json("BUS105")
