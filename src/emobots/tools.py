import openai


def message2string(m, name):
    name = "Other" if m["role"] == "user" else name
    return f"{name}: {m['content']}"


def get_chat_history(chat_messages, name):
    return "\n".join(
        [message2string(m, name) for m in chat_messages if m["role"] != "system"]
    )


def strip_response(response, name):
    response = response.strip()
    response = response.strip("\"'")
    response = response.lstrip(f"{name}: ")
    response = response.strip("\"'")
    return response


def get_name_from_description(client, description):
    name_query_promt = f"Please state the name of the person descriped: {description}. It is important, just the name, nothing more. Only the name."
    messages = [
        {"role": "system", "content": name_query_promt},
    ]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.0
    )
    response = completion.choices[0].message.content

    response = response.strip()
    response = response.strip(".!?\"'")

    name = response

    return response


def get_age_from_description(client, description):
    name_query_promt = f"Please state the age of the person descriped: {description}. It is important, just the name, nothing more. Only the name."
    messages = [
        {"role": "system", "content": name_query_promt},
    ]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.0
    )
    response = completion.choices[0].message.content

    response = response.strip()
    response = response.strip(".!?\"'")

    age = response

    return age
