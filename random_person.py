import openai

from api_key import api_key
from lib.emobot import Emobot

from lib.random_person import create_random_person_description

from lib.tools import get_name_from_description

openai.api_key = api_key

person_desc = create_random_person_description()
name = get_name_from_description(person_desc)

print(person_desc)

bot = Emobot(name, person_desc)

bot.interaction_loop()
