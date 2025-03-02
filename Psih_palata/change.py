
from refresh   import read_data, change_info_file
from error     import exception_menu_item, exception_name, exception_id
from global_v  import file_personal, file_patients

def get_value(message):
    while True:
        value = input(message)
        if exception_menu_item(value):
            return int(value)
        else:
            print("\n", "-"*20, "Invalid number, repeat input", "-"*20)


def get_name(message):
    while True:
        value = input(message)
        if exception_name(value):
            return value
        else:
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)


def get_id(message):
    while True:
        value = input(message)
        if exception_id(value):
            return value
        else:
            print("\n", "-"*20, "Invalid id, repeat input", "-"*20)


def to_continee(messege):
    input(messege)


def menu_change_info_p():
    id = get_id("Input id patient: ")
    data = read_data(file_patients)
    if data[0] == 0:
        return ""
    for i in data:
        i_temp = i.replace("\n", '').split(';')
        if i_temp[0] == id:
            print(
                f"patient found - {i_temp[1]} {i_temp[2]}, diagnosis  - {i_temp[3]}, chamber - {i_temp[4]}")
            id, last_name, first_name, diagnosis, chamber, size_cp, status = i_temp
            break
    else:
        return print("The id is missing!")
    print()
    print("1 last_name", "2 first_name", "3 diagnosis", "4 chamber",
          "5 size_cp", "6 status", "7 return to the previous menu",  sep="\n")
    num = get_value("\n Select item for change: ")
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue press Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue press Enter")
        case 3:
            diagnosis = get_name('Input diagnosis: ')
            to_continee("To continue press Enter")
        case 4:
            chamber = get_value('Input chamber: ')
            to_continee("To continue press Enter")
        case 5:
            size_cp = get_name('Input size_cp: ')
            to_continee("To continue press Enter")
        case 6:
            status = get_name('Input  status: ')
            to_continee("To continue press Enter")
        case 7:
            # patient_menu()
            return 0
    change_info_file(file_patients, id, last_name, first_name,
                     diagnosis, chamber, size_cp, status)


def menu_change_info_s():
    id = get_id("Input id employee: ")
    data = read_data('Personal.csv')
    if data[0] == 0:
        return print('error')
    for i in data:
        i_temp = i.replace("\n", '').split(';')
        if i_temp[0] == id:
            print(
                f" employee - {i_temp[1]} {i_temp[2]}, specialization  - {i_temp[3]}, telephone - {i_temp[4]}")
            id, last_name, first_name, specialization, telephone, place, patient = i_temp
            break
    else:
        return print("The id is missing!")
    print()
    print("1 last_name", "2 first_name", "3 specialization", "4 telethone",
          "5 place", "6 patient ", "7 return to the previous menu",  sep="\n")
    num = get_value("\n Select item for change: ")
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue press Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue press Enter")
        case 3:
            specialization = get_name('Input specialization: ')
            to_continee("To continue press Enter")
        case 4:
            telephone = get_value('Input telethone: ')
            to_continee("To continue press Enter")
        case 5:
            place = get_name('Input parking place number: ')
            to_continee("To continue press Enter")
        case 6:
            patient = get_name('Input  patient: ')
            to_continee("To continue press Enter")
        case 7:
            # personal_menu()
            return 0

    change_info_file('Personal.csv', id, last_name, first_name,
                     specialization, telephone, place, patient)
