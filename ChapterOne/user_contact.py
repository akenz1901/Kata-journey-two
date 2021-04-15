customer_infos = []


def contact():
    user_name = input(str("Enter Name: "))
    user_age = input(str("Enter Your Age: "))
    user_phone = input(str("Enter Phone: "))

    return user_name, user_age, user_phone


def store(take):
    name, age, phone = contact()
    take.append(name, age, phone)


for _ in range(3):
    store(customer_infos)


def new_contact_safe():
    for i in range(3):
        name = input(str("Enter Name: "))
        age = input(str("Enter Your Age: "))
        phone = input(str("Enter Phone: "))
        customer_infos.append((name, age, phone))
    return customer_infos


print(new_contact_safe())