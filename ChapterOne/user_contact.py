new_range = 0
new_details = {}
list_of_Clients = []

while new_range < 3:
    user_name = input(str("Enter Name: "))
    user_age = input(str("Enter Your Age: "))
    user_phone = input(str("Enter Phone: "))
    details = {'name': user_name, 'age': user_age, 'phone': user_phone}
    list_of_Clients.append(details)
    new_range += 1
print(list_of_Clients)
