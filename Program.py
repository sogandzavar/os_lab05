student_list = [
    {"first_name": "Behnam", "last_name": "Moayedi", "id": 14021251328},
    # {"first_name": "Ali", "last_name": "Akbari", "id": 14023551328}     Mesal bood ino velesh khodeto benvis
]

def sort(student_list):
    ask = True
    while ask:
        try:
            choice = int(input(f"\n[1] sort by first name   [2] sort by last name   [3] sort by id\nYour choice: "))
            if choice not in [1, 2, 3]:
                raise ValueError
            match choice:
                case 3:
                    insertion_sort(student_list, "id")
                case 1:
                    insertion_sort(student_list, "first_name")
                case 2:
                    insertion_sort(student_list, "last_name")

        except ValueError:
            print("Invalid choice")
            

def insertion_sort(student_list, key_name):
    for i in range(1, len(student_list)):
        key_item = student_list[i]
        j = i - 1
        while j >= 0 and str(student_list[j][key_name]).lower() > str(key_item[key_name]).lower():
            student_list[j + 1] = student_list[j]
            j -= 1
        student_list[j + 1] = key_item

    print("\nSorted list:")
    for s in student_list:
        print(s["first_name"], s["last_name"], s["id"])

sort(student_list)
