import openai

from emobots.intention import intention_analysis
from emobots.mood import mood_analysis
from emobots.tools import message2string, strip_response


class Emobot:
    def __init__(self, client, name, person_desc) -> None:
        self.client = client
        self.name = name
        self._reccurrent_system_prompt = f"This is {name}: {person_desc}."

        self._mood_analyis_system_prompt = f"""
        From the above conversation, what do you think is the current mood of {name}?
        If uncertain, simply state that the mood is unknown."""

        self._intention_analyis_system_prompt = f"""
        From the above conversation, what does {name} wants to do from these options?
        1. keep the conversation going
        2. stop the converstation
        3. wait for the other person to say more
        4. accept the other persons offer

        Just give the number.
        If uncertain, simply state 'None'.
        """

        self.chat_messages = []

        self.current_feeling = "Neutral."

    def interaction_step(
        self,
        chat_messages,
        current_feeling,
        reccurrent_system_prompt,
        intention_analyis_system_prompt,
        mood_analyis_system_prompt,
    ):
        user_input = input("you: ")

        chat_messages.append({"role": "user", "content": user_input})
        # !!! maybe this is important
        # chat_messages.append(
        #    {"role": "system", "content": reccurrent_system_prompt + current_feeling}
        # )

        chat_history = "\n".join(
            [
                message2string(m, self.name)
                for m in chat_messages
                if m["role"] != "system"
            ]
        )

        messages = []

        messages.append(
            {
                "role": "system",
                "content": reccurrent_system_prompt
                + "\n"
                + f"{self.name} is feeling: "
                + current_feeling
                + "\n"
                + "Also, this chat history is given: \n"
                + chat_history
                + f"\{self.name}: ",
            }
        )
        messages.append(
            {
                "role": "user",
                "content": f"""Complete what {self.name}
                would say in a style and grammar that matches
                their background, but only a single or a few sentences.""",
            }
        )

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, temperature=0.3
        )
        response = completion.choices[0].message.content

        # response = strip_response(response, self.name)
        print(f"{self.name}:", end=" ")
        for x in response:
            print(x, end="")

        print()

        # print(f"{self.name}:", response)
        chat_messages.append({"role": "assistant", "content": response})

        mood_analysis_response = mood_analysis(
            self.client, self.name, chat_messages, mood_analyis_system_prompt
        )

        current_feeling = mood_analysis_response
        print(f"({mood_analysis_response})")

        intention_analysis_response = intention_analysis(
            self.client, self.name, chat_messages, intention_analyis_system_prompt
        )

        print(f"(intention: {intention_analysis_response})")

        return response, intention_analysis_response

    def interaction_loop(self):
        running = True
        while running is True:
            response, intention = self.interaction_step(
                self.chat_messages,
                self.current_feeling,
                self._reccurrent_system_prompt,
                self._intention_analyis_system_prompt,
                self._mood_analyis_system_prompt,
            )

            if "2" in intention:
                print("You have been dismissed!")
                return 2

            if "4" in intention:
                print("Your offer has been accepted!")
                return 4
