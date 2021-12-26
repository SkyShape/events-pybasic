from datetime import datetime


def time_date(elem):
    return datetime(year=int(elem[4:8]), month=int(elem[2:4]), day=int(elem[0:2]), hour=int(elem[8:10]),
                    minute=int(elem[10:]))


def get_word_in_list_of_dic(word, list_of_dic, key):
    word_in_dict = False
    for dictionary in list_of_dic:
        if key == "title":
            title = dictionary[key]
            if title == word.strip().lower().capitalize():
                word_in_dict = True
    return word_in_dict


lis_events = []


def make_dic_word(word, dic_temp, key):
    if word:
        if key == "title":
            if not get_word_in_list_of_dic(word, lis_events, key):
                dic_temp[key] = word
            elif get_word_in_list_of_dic(word, lis_events, key):
                print(f"You have {word} in {key.replace('-', ' ')} events. ")
                # time.sleep(2)
                print_menu()
            else:
                print("error")
        elif key == "start-time":
            word = "".join(filter(str.isdigit, word))
            if len(word) == 12:
                now = datetime.now()
                word_date = time_date(word)
                if word_date > now:
                    dic_temp[key] = word
                    for dictionary in lis_events:
                        if len(dictionary[key]) == 12:
                            start_date = time_date(dictionary["start-time"])
                            end_date = time_date(dictionary["end-time"])
                            if start_date <= word_date <= end_date:
                                print("You have events in that period of time...")
                                print_menu()
                            else:
                                dic_temp[key] = word
                        else:
                            dic_temp[key] = word

                else:
                    print("Your date is in past...")
                    print_menu()
            else:
                print("You have write wrong time...")
                print_menu()
        elif key == "end-time":
            word = "".join(filter(str.isdigit, word))
            if len(word) == 12:
                now = datetime.now()
                word_date = time_date(word)
                if word_date > now:
                    dic_temp[key] = word
                    for dictionary in lis_events:
                        start_date = time_date(dictionary["start-time"])
                        end_date = time_date(dictionary["end-time"])
                        if start_date <= word_date <= end_date:
                            print("You have events in that period of time...")
                            print_menu()
                        elif word_date > time_date(dic_temp["start-time"]):
                            dic_temp[key] = word
                        else:
                            print("You write the wrong end time...")
                            add_event()
                else:
                    print("Your date is in past...")
                    print_menu()
            else:
                print("You have write wrong time...")
                print_menu()
        else:
            print("Error in dictionary...")

    else:
        print(f"You must to write {key.replace('-', ' ')} event...")
        print_menu()


def add_event():
    while True:
        command = input("Do you want to make an event?Y/N \n").strip().lower()
        dic_temp = {"title": "", "start-time": "", "end-time": ""}
        if command == "y":
            command = input("What is your event title? \n").strip().lower().capitalize()
            make_dic_word(command, dic_temp, "title")
            command = input("What is your event start time? DD.MM.YYYY, hour:minute \n")
            make_dic_word(command, dic_temp, "start-time")
            command = input("What is your event end time? DD.MM.YYYY, hour:minute \n")
            make_dic_word(command, dic_temp, "end-time")
            print(dic_temp)
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
        command = input().strip(". ").lower()
        match command:
            case "a":
                add_event()
            case "e":
                break
            case _:
                print("to be continue...")


print_menu()
