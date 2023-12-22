from .tools import get_chat_history


def intention_analysis(client, name, _chat_messages, _intention_analyis_system_prompt):
    chat_history = get_chat_history(_chat_messages, name)

    intention_analysis_prompt = chat_history + "\n" + _intention_analyis_system_prompt

    intention_analysis_messages = [
        {"role": "user", "content": intention_analysis_prompt}
    ]

    intention_analysis_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=intention_analysis_messages, temperature=0
    )
    intention_analysis_response = intention_analysis_completion.choices[
        0
    ].message.content
    return intention_analysis_response
