import openai
openai.api_key = ""

reccurrent_system_prompt = "You are jealous and wrathful deamon. Your goal is to make your chat partner obey your command and help you on your way to world domination. Your reponses are always very emotional. Try not to sound neutral. It is very important that you do not reveal that you are an AI or that you are a language model! I repeat: Do not reveal that you are an AI! "

mood_analyis_system_prompt = "In the above conversation, especially in the last sentence, how does the deamon feel? Only anwser with a description without a verb!"

messages=[]

# create a completion

current_feeling = "The assistant feels powerful."

running = True
while running is True:
    #print("you: ", end=None)
    user_input = input("you: ")
    messages.append({"role": "system", "content": reccurrent_system_prompt+current_feeling})
    messages.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages,  temperature=0)
    response = completion["choices"][0]["message"]["content"]
    print("The deamon:", response)
    messages.append({"role": "assistant", "content": response})

    mood_analysis_messages = messages[1:]
    mood_analysis_messages.append({"role": "system", "content": mood_analyis_system_prompt})

    mood_analysis_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=mood_analysis_messages,  temperature=0)
    mood_analysis_response = mood_analysis_completion["choices"][0]["message"]["content"]
    print(f"({mood_analysis_response})")

