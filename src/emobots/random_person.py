import openai
import random

from .data import random_character_traits


def create_random_person_description(temperature=1.0):
    inspiration = ", ".join(random.sample(random_character_traits, 3))
    gender = random.choice(["male", "female"])
    age = random.randint(18, 72)
    person_generation_prompt = f"Please generate a fictious description of a {inspiration} person ({gender}, {age} years old) located anywhere on the planet, chatting in the internet. State their name, age, gender, where they are from, hobbies, family etc. Also describe their mission why they are in the internet and their current mood."
    messages = [
        {"role": "system", "content": person_generation_prompt},
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=temperature
    )
    response = completion["choices"][0]["message"]["content"]
    return response


def create_random_person_description_tinder(
    gender_list=["female", "male"], age_min=18, age_max=72, temperature=1.0
):
    inspiration = ", ".join(random.sample(random_character_traits, 3))
    gender = random.choice(gender_list)
    age = random.randint(age_min, age_max)
    person_generation_prompt = f"Please generate a fictious description of a {inspiration} person ({gender}, {age} years old) located anywhere on the planet, using tinder. State their name, age, gender, where they are from, hobbies, family etc. Describe their profile picture. Also describe their mission why they are on tinder and their current mood."
    messages = [
        {"role": "system", "content": person_generation_prompt},
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=temperature
    )
    response = completion["choices"][0]["message"]["content"]

    return response
