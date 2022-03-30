first_txt = open('nsc508s t1_22-1.txt', 'r')


list_of_number = [str(i) for i in range(1, 11)]

dic = {list_of_number.pop(0): dd.strip() for dd in first_txt}

print(dic)

first_txt.close()
