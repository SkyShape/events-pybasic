import time


def get_word_in_list_of_dic(word, list_of_dic, key):
    word_in_dict = False
    for dictionary in list_of_dic:
        title = dictionary[key]
        if title == word.strip().lower().capitalize():
            word_in_dict = True

    return word_in_dict


lis_events = []


def make_dic_word(word, dic_temp, key):
    if word:
        if not get_word_in_list_of_dic(word, lis_events, key):
            dic_temp[key] = word
        elif get_word_in_list_of_dic(word, lis_events, key):
            print(f"You have {word} in {key.replace('-', ' ')} events. ")
            # time.sleep(2)
            print_menu()
        else:
            print("error")
    else:
        print(f"You must to write {key.replace('-', ' ')} event...")


def add_event():
    while True:
        command = input("Do you want to make an event?Y/N \n").strip().lower()
        if command == "y":
            dic_temp = {"title": "", "start-time": "", "end-time": ""}
            command = input("What is your event title? \n").strip().lower().capitalize()
            make_dic_word(command, dic_temp, "title")
            command = input("What is your event start time? \n")
            make_dic_word(command, dic_temp, "start-time")
            command = input("What is your event end time? \n")
            make_dic_word(command, dic_temp, "end-time")
            # print(dic_temp)
            lis_events.append(dic_temp)
        elif command == "n":
            print("Have a nice day!")
            break
        else:
            print("You didn`t make a right answer...")
            print_menu()

    print(lis_events)


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
