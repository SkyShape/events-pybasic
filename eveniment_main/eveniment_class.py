# Lista de feature-uri este in functia print_menu.
# Orice adaugare sau modificare se face doar daca
# noul eveniment nu se suprapune cu alte evenimente.

#  AAAAAAAA
#    BBB
#
#  AAAAA
# BBBB
#
#  AAAAA
#    BBBB
#
#  AAAA
# BBBBBB
# caz valid in care acceptam adaugarea/modificarea evenimentului.
# AAAAA
#        BBBBB

# class Event:
#     def __init__(self, title, start_datetime, end_datetime):
#         pass

def get_word_in_list_of_dic(word: str, list_of_dic: list, key="title"):
    word_in_dict = False
    for dictionary in list_of_dic:
        title = dictionary[key]
        if title == word.strip().lower().capitalize():
            word_in_dict = True
    return word_in_dict


def make_dic_word(word, key="title"):
    if word:
        if not get_word_in_list_of_dic(word, lis_events, key):
            dic_temp[key] = word
        elif get_word_in_list_of_dic(word, lis_events, key):
            print(f"You have {word} in {key} ")
        else:
            print("error")
    else:
        print("You must to write title event...")


lis_events = []
dic_temp = {"title": "", "start-time": "", "end-time": ""}


def add_event():
    while True:
        command = input("Do you want to make an event?Y/N \n").strip().lower()
        if command == "y":
            command = input("What is your event title? \n").strip().lower().capitalize()
            make_dic_word(command, "title")
            command = input("What is your event start time? \n")
            make_dic_word(command, "start-time")
            command = input("What is your event end time? \n")
            make_dic_word(command, "end-time")
            lis_events.append(dic_temp)
        elif command == "n":
            print("Have a nice day!")
            break
        else:
            print("You didn`t make a right answer...")
            continue


    print(lis_events)


# class Events:
#     def __init__(self, title, start_time, end_time):
#         self.dic_event = {
#             "title": title,
#             "start-time": start_time,
#             "end-time": end_time
#         }
#
#     def __str__(self):
#         return f"Event is {self.dic_event['title']} and start in {self.dic_event['start-time']} and finish in {self.dic_event['end-time']}"
#
#     def append_event_in_list(self, list):
#         return list.append(self.dic_event)

# list_events = []
# Andrei_20 = Event("Andrei event", 20, 100)
# print(Andrei_20)
# Andrei_20.append_event_in_list(list_events)
# print(list_events)

# while True:
#     list_event = []
#     title_event = (input("What is your event name: ")).strip().capitalize()
#     print(title_event)
#     break


def print_menu():
    while True:
        print('\t Welcome!!! \n Please select your menu:')
        print('\ta. Create event')
        print('\tb. Listings events')
        print('\tc. Delete event')
        print('\td. Edit event')
        print('\te. Exit menu')
        comand = input().strip(". ").lower()
        match comand:
            case "a":
                add_event()
            case "e":
                break
            case _:
                print("to be continue...")


print_menu()
