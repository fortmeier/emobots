import logging

logging.basicConfig(
    filename="openai_output.log", encoding="utf-8", level=logging.DEBUG, force=True
)


from openai import OpenAI


def test_openai_api():
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # If not set, it will raise an error so make sure to set it
    # in your environment variables.
    client = OpenAI()

    assert client


def test_openai_api_call():
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # If not set, it will raise an error so make sure to set it
    # in your environment variables.
    client = OpenAI()

    messages = [{"role": "user", "content": "Hi"}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.0
    )

    assert response.choices[0].message.content != None

    logging.info(
        response.choices[0].message.content,
    )
