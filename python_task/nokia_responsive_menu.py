# nokia_responsive_menu.py

menu_message = """
List of menu functions

1. Phone Book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. Sim services

Press 0 to end the app
"""

phone_book = """
1. Phone book
  1. Search
  2. Service Nos.
  3. Add name
  4. Erase
  5. Edit
  6. Assign tone
  7. Send b'card
  8. Options
  9. Speed dials
  10. Voice tags

Press 0 to go back
"""

phone_book_options = """
8. Options
  1. Type of view
  2. Memory status

Press 0 to go back
"""

messages = """
2. Messages
  1. Write messages
  2. Inbox
  3. Outbox
  4. Picture messages
  5. Templates
  6. Smileys
  7. Message settings
  8. Info service
  9. Voice mailbox number
  10. Service command editor

Press 0 to go back
"""

message_settings = """
1. Set 1
2. Common

Press 0 to go back
"""

set_1 = """
1. Set 1
  1. Message center number
  2. Messages sent as
  3. Message validity

Press 0 to go back
"""

common = """
2. Common
  1. Delivery reports
  2. Reply via same centre
  3. Character support

Press 0 to go back
"""

call_register = """
Call Register
1. Missed Calls
2. Received Calls
3. Dialled Numbers
4. Erase Recent Call Lists
5. Show Call Duration
6. Show Call Costs
7. Call Cost Settings
8. Prepaid Credit

Press 0 to go back
"""

show_call_duration = """
Show Call Duration
1. Last Call Duration
2. All Calls' Duration
3. Received Calls' Duration
4. Dialled Calls' Duration
5. Clear Timers

Press 0 to go back
"""

show_call_costs = """
Show Call Costs
1. Last Call Cost
2. All Calls' Cost
3. Clear Counters

Press 0 to go back
"""

call_cost_settings = """
Call Cost Settings
1. Call Cost Limit
2. Show Costs In

Press 0 to go back
"""

tones = """
Tones
1. Ringing Tone
2. Ringing Volume
3. Incoming Call Alert
4. Composer
5. Message Alert Tone
6. Keypad Tones
7. Warning And Game Tones
8. Vibrating Alert
9. Screen Saver

Press 0 to go back
"""

settings = """
Settings
1. Call Settings
2. Phone Settings
3. Security Settings
4. Restore Factory Settings

Press 0 to go back
"""

call_settings = """
Call Settings
1. Automatic Redial
2. Speed Dialling
3. Call Waiting Options
4. Own Number Sending
5. Phone Line In Use
6. Automatic Answer

Press 0 to go back
"""

phone_settings = """
Phone Settings
1. Language
2. Cell Info Display
3. Welcome Note
4. Network Selection
5. Lights
6. Confirm SIM Service Actions

Press 0 to go back
"""

security_settings = """
Security Settings
1. PIN Code Request
2. Call Barring Service
3. Fixed Dialling
4. Closed User Group
5. Phone Security
6. Change Access Codes

Press 0 to go back
"""

clock = """
Clock
1. Alarm Clock
2. Clock Settings
3. Date Settings
4. Stopwatch
5. Countdown Timer
6. Auto Update Of Date And Time

Press 0 to go back
"""

while True:
    print(menu_message)
    main_menu_input = int(input("Please Enter your preferred number from the options: "))

    if main_menu_input == 0:
    	   print("Goodbye! Enjoy your day")
    	   break

    if main_menu_input < 0 or main_menu_input > 13:
        print("Invalid Input!! Enter a valid number from the options")
        continue

    match main_menu_input:
        case 1:
            while True:
                print(phone_book)
                phone_book_input = int(input("Enter your preferred number: "))
                if phone_book_input == 0:
                    break
                elif phone_book_input < 0 or phone_book_input > 10:
                    print("Invalid input! Try again.")
                    continue

                match phone_book_input:
                    case 1:
                        print("Search")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 2:
                        print("Service Nos.")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 3:
                        print("Add name")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 4:
                        print("Erase")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 5:
                        print("Edit")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 6:
                        print("Assign tone")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 7:
                        print("Send b'card")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 8:
                        while True:
                            print(phone_book_options)
                            phone_book_options_input = int(input("Please Enter your preferred number from the options: "))
                            if phone_book_options_input < 0 or phone_book_options_input > 2:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            match phone_book_options_input:
                                case 1:
                                    print("Type of view")
                                    while True:
                                        back = int(input("Press 0 to go back: "))
                                        if back == 0:
                                            break
                                        print("Invalid input! Please press 0 to go back.")
                                    continue
                                case 2:
                                    print("Memory status")
                                    while True:
                                        back = int(input("Press 0 to go back: "))
                                        if back == 0:
                                            break
                                        print("Invalid input! Please press 0 to go back.")
                                    continue
                                case 0:
                                    break
                        continue
                    case 9:
                        print("Speed dials")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 10:
                        print("Voice tags")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue

        case 2:
            while True:
                print(messages)
                messages_input = int(input("Please Enter your preferred number from the options: "))
                if messages_input == 0:
                    break
                elif messages_input < 0 or messages_input > 10:
                    print("Invalid input! Enter a valid number from the options.")
                    continue

                match messages_input:
                    case 1:
                        print("Write messages")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 2:
                        print("Inbox")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 3:
                        print("Outbox")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 4:
                        print("Picture messages")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 5:
                        print("Templates")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 6:
                        print("Smileys")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 7:
                        while True:
                            print(message_settings)
                            message_settings_input = int(input("Please Enter your preferred number from the options: "))
                            if message_settings_input < 0 or message_settings_input > 2:
                                print("Invalid input! Enter a valid number from the options.")
                                continue

                            match message_settings_input:
                                case 1:
                                    while True:
                                        print(set_1)
                                        set_1_input = int(input("Please Enter your preferred number from the options: "))
                                        if set_1_input < 0 or set_1_input > 3:
                                            print("Invalid input! Enter a valid number from the options.")
                                            continue

                                        match set_1_input:
                                            case 1:
                                                print("Message center number")
                                                while True:
                                                    back = int(input("Press 0 to go back: "))
                                                    if back == 0:
                                                        break
                                                    print("Invalid input! Please press 0 to go back.")
                                                continue
                                            case 2:
                                                print("Messages sent as")
                                                while True:
                                                    back = int(input("Press 0 to go back: "))
                                                    if back == 0:
                                                        break
                                                    print("Invalid input! Please press 0 to go back.")
                                                continue
                                            case 3:
                                                print("Message validity")
                                                while True:
                                                    back = int(input("Press 0 to go back: "))
                                                    if back == 0:
                                                        break
                                                    print("Invalid input! Please press 0 to go back.")
                                                continue
                                            case 0:
                                                break
                                    continue
                                case 2:
                                    while True:
                                        print(common)
                                        common_input = int(input("Please Enter your preferred number from the options: "))
                                        if common_input < 0 or common_input > 3:
                                            print("Invalid input! Enter a valid number from the options.")
                                            continue

                                        match common_input:
                                            case 1:
                                                print("Delivery reports")
                                                while True:
                                                    back = int(input("Press 0 to go back: "))
                                                    if back == 0:
                                                        break
                                                    print("Invalid input! Please press 0 to go back.")
                                                continue
                                            case 2:
                                                print("Reply via same centre")
                                                while True:
                                                    back = int(input("Press 0 to go back: "))
                                                    if back == 0:
                                                        break
                                                    print("Invalid input! Please press 0 to go back.")
                                                continue
                                            case 3:
                                                print("Character support")
                                                while True:
                                                    back = int(input("Press 0 to go back: "))
                                                    if back == 0:
                                                        break
                                                    print("Invalid input! Please press 0 to go back.")
                                                continue
                                            case 0:
                                                break
                                    continue
                                case 0:
                                    break
                        continue
                    case 8:
                        print("Info service")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 9:
                        print("Voice mailbox number")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue
                    case 10:
                        print("Service command editor")
                        while True:
                            back = int(input("Press 0 to go back: "))
                            if back == 0:
                                break
                            print("Invalid input! Please press 0 to go back.")
                        continue

        case 3:
            print("Chat")
            while True:
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                print("Invalid input! Please press 0 to go back.")
            continue
            
     
        case 4:
            while True:
                print(call_register)
                call_register_input = int(input("Please Enter your preferred number from the options: "))

                if call_register_input < 0 or call_register_input > 8:
                    print("Invalid Input!! Enter a valid number from the options")
                    continue

                if call_register_input == 0:
                    break

                match call_register_input:
                    case 1:
                        print("Missed calls")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 2:
                        print("Received calls")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 3:
                        print("Dialled numbers")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 4:
                        print("Erase recent call lists")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 5:
                        while True:
                            print(show_call_duration)
                            show_call_duration_input = int(input("Please Enter your preferred number from the options: "))

                            if show_call_duration_input < 0 or show_call_duration_input > 5:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            if show_call_duration_input == 0:
                                break

                            match show_call_duration_input:
                                case 1:
                                    print("Last call Duration")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 2:
                                    print("All calls' duration")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 3:
                                    print("Received calls' duration")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 4:
                                    print("Dialled calls' duration")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 5:
                                    print("Clear timers")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                    case 6:
                        while True:
                            print(show_call_costs)
                            show_call_costs_input = int(input("Please Enter your preferred number from the options: "))

                            if show_call_costs_input < 0 or show_call_costs_input > 3:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            if show_call_costs_input == 0:
                                break

                            match show_call_costs_input:
                                case 1:
                                    print("Last call cost")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 2:
                                    print("All call cost")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 3:
                                    print("Clear counters")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                    case 7:
                        while True:
                            print(call_cost_settings)
                            call_cost_settings_input = int(input("Please Enter your preferred number from the options: "))

                            if call_cost_settings_input < 0 or call_cost_settings_input > 2:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            if call_cost_settings_input == 0:
                                break

                            match call_cost_settings_input:
                                case 1:
                                    print("Call cost limit")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                                case 2:
                                    print("Show costs in")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                    continue

                    case 8:
                        print("Prepaid credit")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

        case 5:
            while True:
                print(tones)
                print("Please Enter your preferred number from the options: ")
                tones_input = int(input())

                if tones_input < 0 or tones_input > 9:
                    print("Invalid Input!! Enter a valid number from the options")
                    continue

                if tones_input == 0:
                    break

                match tones_input:
                    case 1:
                        print("Ringing tone")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 2:
                        print("Ringing volume")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 3:
                        print("Incoming call alert")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 4:
                        print("Composer")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 5:
                        print("Message alert tone")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 6:
                        print("Keypad tones")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 7:
                        print("Warning and game tones")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 8:
                        print("Vibrating alert")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 9:
                        print("Screen saver")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue
                        
        case 6:
            while True:
                print(settings)
                print("Please Enter your preferred number from the options: ")
                settings_input = int(input())

                if settings_input < 0 or settings_input > 4:
                    print("Invalid Input!! Enter a valid number from the options")
                    continue

                if settings_input == 0:
                    break

                match settings_input:
                    case 1:
                        while True:
                            print(call_settings)
                            print("Please Enter your preferred number from call settings options: ")
                            call_settings_input = int(input())

                            if call_settings_input < 0 or call_settings_input > 6:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            if call_settings_input == 0:
                                break

                            match call_settings_input:
                                case 1:
                                    print("Automatic redial")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 2:
                                    print("Speed dialling")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 3:
                                    print("Call waiting options")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 4:
                                    print("Own number sending")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 5:
                                    print("Phone line in use")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 6:
                                    print("Automatic answer")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")

                    case 2:
                        while True:
                            print(phone_settings)
                            print("Please Enter your preferred number from phone settings options: ")
                            phone_settings_input = int(input())

                            if phone_settings_input < 0 or phone_settings_input > 6:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            if phone_settings_input == 0:
                                break

                            match phone_settings_input:
                                case 1:
                                    print("Language")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 2:
                                    print("Cell info display")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 3:
                                    print("Welcome note")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 4:
                                    print("Network selection")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 5:
                                    print("Lights")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 6:
                                    print("Confirm SIM service actions")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")

                    case 3:
                        while True:
                            print(security_settings)
                            print("Please Enter your preferred number from security settings options: ")
                            security_settings_input = int(input())

                            if security_settings_input < 0 or security_settings_input > 6:
                                print("Invalid Input!! Enter a valid number from the options")
                                continue

                            if security_settings_input == 0:
                                break

                            match security_settings_input:
                                case 1:
                                    print("PIN code request")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 2:
                                    print("Call barring service")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 3:
                                    print("Fixed dialling")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 4:
                                    print("Closed user group")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 5:
                                    print("Phone security")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")
                                case 6:
                                    print("Change access codes")
                                    while True:
                                        print("Press 0 to go back")
                                        back = int(input())
                                        if back == 0:
                                            break
                                        else:
                                            print("Invalid input! Please press 0 to go back.")

                    case 4:
                        print("Restore factory settings")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")

        case 7:
            while True:
                print("Call divert")
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                else:
                    print("Invalid input! Please press 0 to go back.")
            continue

        case 8:
            while True:
                print("Games")
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                else:
                    print("Invalid input! Please press 0 to go back.")
            continue

        case 9:
            while True:
                print("Calculator")
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                else:
                    print("Invalid input! Please press 0 to go back.")
            continue

        case 10:
            while True:
                print("Reminders")
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                else:
                    print("Invalid input! Please press 0 to go back.")
            continue

        case 11:
            while True:
                print(clock)
                print("Please Enter your preferred number from the options: ")
                clock_input = int(input())

                if clock_input < 0 or clock_input > 6:
                    print("Invalid Input!! Enter a valid number from the options")
                    continue
                    
                if clock_input == 0:
                		break

                match clock_input:
                    case 1:
                        print("Alarm clock")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 2:
                        print("Clock settings")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 3:
                        print("Date setting")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 4:
                        print("Stopwatch")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 5:
                        print("Countdown timer")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 6:
                        print("Auto update of date and time")
                        while True:
                            print("Press 0 to go back")
                            back = int(input())
                            if back == 0:
                                break
                            else:
                                print("Invalid input! Please press 0 to go back.")
                        continue

                    case 0:
                        continue

        case 12:
            while True:
                print("Profiles")
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                else:
                    print("Invalid input! Please press 0 to go back.")
            continue

        case 13:
            while True:
                print("SIM services")
                print("Press 0 to go back")
                back = int(input())
                if back == 0:
                    break
                else:
                    print("Invalid input! Please press 0 to go back.")
            continue
