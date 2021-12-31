import json
import os
from datetime import datetime
from pprint import pprint


def is_file_empty(f_path):
    # Check if file is empty, is size is 0 bytes
    return os.stat(f_path).st_size == 0


lis_events = []

if os.path.exists('events.json'):
    with open("events.json") as file:
        file_path = 'events.json'
        is_empty = is_file_empty(file_path)
        if not is_empty:
            lis_events = json.load(file)
else:
    lis_events = []


def make_start_time(word, dic_temp, key):
    if len(word) == 12:
        now = datetime.now()
        word_date = time_date(word)
        if word_date:
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


def time_date(elem):
    try:
        return datetime(year=int(elem[4:8]), month=int(elem[2:4]), day=int(elem[0:2]), hour=int(elem[8:10]),
                        minute=int(elem[10:]))
    except ValueError or TypeError:
        print("We have an error on your date time, please rewrite.")
        print_menu()


def event_time_check(time, list_dictionary):
    # dictionary from list will use time-start and time-end like keys
    # if the list is empty we will get a true value
    new_time = time_date(time)
    now_time = datetime.now()
    if len(list_dictionary) != 0:
        for i in range(len(list_dictionary)):
            if new_time > now_time:
                if len(list_dictionary[i]["end-time"]) == 12:
                    end_time = time_date(list_dictionary[i]["end-time"])
                    if len(list_dictionary[i]["start-time"]) == 12:
                        start_time = time_date(list_dictionary[i]["start-time"])
                        if start_time <= new_time <= end_time:
                            return False
                        else:
                            return True
                else:
                    return False
            else:
                return False
    elif new_time > now_time:
        return True
    else:
        return False


def get_word_in_list_of_dic(word, list_of_dic, key):
    word_in_dict = False
    for dictionary in list_of_dic:
        if key == "title":
            title = dictionary[key]
            if title == word.strip().lower().capitalize():
                word_in_dict = True
    return word_in_dict


def make_dic_word(word, dic_temp, key):
    if word:
        if key == "title":
            if not get_word_in_list_of_dic(word, lis_events, key):
                dic_temp[key] = word
            elif get_word_in_list_of_dic(word, lis_events, key):
                print(f"You have {word} in {key.replace('-', ' ')} events. ")
                print_menu()
            else:
                print("error")
        elif key == "start-time":
            word = "".join(filter(str.isdigit, word))
            if len(word) == 12:
                if event_time_check(word, lis_events):
                    dic_temp[key] = word
                else:
                    print("Your time is wrong...")
                    print_menu()
            else:
                print("You have write wrong time...")
                print_menu()
        elif key == "end-time":
            word = "".join(filter(str.isdigit, word))
            if len(word) == 12:
                if event_time_check(word, lis_events):
                    dic_temp[key] = word
                else:
                    print("Your time is wrong...")
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
            try:
                command = input("What is your event title? \n").strip().lower().capitalize()
                make_dic_word(command, dic_temp, "title")
                command = input("What is your event start time? DD.MM.YYYY, hour:minute \n")
                make_dic_word(command, dic_temp, "start-time")
                command = input("What is your event end time? DD.MM.YYYY, hour:minute \n")
                make_dic_word(command, dic_temp, "end-time")
                print(dic_temp)
                lis_events.append(dic_temp)
                if dic_temp:
                    with open("events.json", 'w') as f:
                        json.dump(lis_events, f)

            except ValueError or TypeError:
                print("We have an error on your date time, please rewrite.")

        elif command == "n":
            print("Have a nice day!")
            break

        else:
            print("You didn`t make a right answer...")
            print_menu()


def print_menu():
    global lis_events
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
            case "b":
                if len(lis_events) < 1 or not lis_events:
                    print("You don`t have events in your file")
                else:
                    for dictionary in lis_events:
                        print(
                            f"{dictionary['title']} start in {time_date(dictionary['start-time'])} and is finished in {time_date(dictionary['end-time'])}")
            case "c":
                command = input("What is title of the event that you want to delete?\n").strip().lower().capitalize()
                if len(lis_events) >= 1:
                    for i in range(len(lis_events)):
                        if lis_events[i]["title"] == command:
                            del lis_events[i]
                            with open('events.json', 'w') as f:
                                json.dump(lis_events, f)
                            print(f"You have deleted {command} event")
                            print_menu()
                        else:
                            print(f"We don`t have '{command}' event in list of events...")
                            print_menu()
                else:
                    print("Your event list is empty...")
                    print_menu()
            case "d":
                command = input("What event do you want to edit?Write title event: \n").strip("")
                if command:
                    if len(lis_events) >= 1:
                        for i in range(len(lis_events)):
                            if lis_events[i]["title"] == command:
                                pprint(lis_events[i])
                                new_lis_events = lis_events
                                dic_temp = lis_events[i]
                                del lis_events[i]
                                print("What do you want to edit?")
                                print('\ta. Title')
                                print('\tb. Start date-time')
                                print('\tc. End date-time')
                                command = input().strip(". ")
                                match command:
                                    case "a":
                                        command = input("What is the new title? \n").strip().capitalize()
                                        dic_temp["title"] = command
                                        lis_events.append(dic_temp)
                                        with open("events.json", 'w') as f:
                                            json.dump(lis_events, f)
                                        print("We edit!")
                                    case "b":
                                        command = input("What is the new start date-time? DD.MM.YYYY, hour:minute\n")
                                        word = "".join(filter(str.isdigit, command))
                                        if event_time_check(word, lis_events) and time_date(word) < time_date(
                                                dic_temp["end-time"]):
                                            dic_temp["start-time"] = word
                                            lis_events.append(dic_temp)
                                            with open("events.json", 'w') as f:
                                                json.dump(lis_events, f)
                                            print("We edit!")
                                        else:
                                            print("You write the wrong time...")
                                            print_menu()
                                    case "c":
                                        command = input("What is the new end date-time? DD.MM.YYYY, hour:minute\n")
                                        word = "".join(filter(str.isdigit, command))
                                        if event_time_check(word, lis_events) and time_date(word) > time_date(
                                                dic_temp["start-time"]):
                                            dic_temp["end-time"] = word
                                            lis_events.append(dic_temp)
                                            with open("events.json", 'w') as f:
                                                json.dump(lis_events, f)
                                            print("We edit!")
                                        else:
                                            print("You write the wrong time...")
                                            print_menu()
                                    case _:
                                        lis_events = new_lis_events
                                        print("You didn`t selected the right menu.")
                                        print_menu()
                    else:
                        print("You don`t have events...")

            case "e":
                exit()
            case _:
                print("You didn`t take the right menu.")
                print_menu()

# use print_menu() function to go through the menu
# print_menu()
