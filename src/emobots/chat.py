def console_interaction_loop_instant(emobot, max_line_length=0):
    running = True
    while running is True:
        input_string = "\x1b[0;31;40m" + "You: " + "\x1b[0m"
        user_input = input(input_string)

        response_generator = emobot.interaction_generator(user_input)

        bot_prompt = "\x1b[0;32;40m" + f"{emobot.name}: " + "\x1b[0m"

        print(bot_prompt, end="")
        current_line_length = 0
        for response in response_generator:
            current_line_length += len(response)
            if max_line_length > 0 and current_line_length > max_line_length:
                print("", end="\n")
                current_line_length = 0

            print(response, end="")

        print("", end="\n")

        intention = emobot.intention

        if "2" in intention:
            print("You have been dismissed!")
            return 2

        if "4" in intention:
            print("Your offer has been accepted!")
            return 4
