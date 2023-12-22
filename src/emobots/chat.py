def console_interaction_loop(emobot):
    running = True
    while running is True:
        input_string = "\x1b[0;31;40m" + "you: " + "\x1b[0m"
        user_input = input(input_string)

        response, intention = emobot.interaction(user_input)

        bot_prompt = "\x1b[0;32;40m" + f"{emobot.name}: " + "\x1b[0m"

        print(bot_prompt, response)

        if "2" in intention:
            print("You have been dismissed!")
            return 2

        if "4" in intention:
            print("Your offer has been accepted!")
            return 4
