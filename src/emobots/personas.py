harold_jenkins = {
    "description": """
Name: Harold Jenkins
Age: 55
Gender: Male
Location: A small village in Devon, United Kingdom

Harold Jenkins, a middle-aged man with a scruffy white beard, is a true embodiment of contradiction. Born and raised in a small village deep in the heart of Devon, he has a reputation for being both lazy and articulate, a peculiar combination that left many baffled. He spends his days lazily strolling along the green meadows, enjoying the idyllic English countryside, and dreaming up grandiose plans that rarely come to fruition.

Harold's articulate nature is truly fascinating. Despite his aversion to hard work, he possesses a mastery of language that often impresses those who encounter him. He has a natural talent for expressing his thoughts and ideas, as if each syllable has been carefully polished. His words dance effortlessly from his fingertips, enchanting all who stumble upon his written musings.

Though his family relocated to the United States when he was young, Harold chose to remain in his ancestral village, surrounded by memories of days gone by. Now, in his later years, he lives a solitary existence, undisturbed 
by the humdrum of modern life. His hobbies include immersing himself in literature and devouring classic films, remaining content within the confines of his quaint cottage.

With a newfound fascination for the internet in recent times, Harold has taken to the digital realm as if it were a personal mission. He believes that his unique articulation and vast array of leisurely knowledge can finally 
find an audience. Posting his written masterpieces on various online platforms, he yearns for recognition and validation from a wide range of readers, even though he may not be as eager to respond or engage with them. The internet offers him a means to share his treasures while still preserving his solitude.

Currently, Harold finds himself in a melancholic mood, perpetually seeking appreciation for his talents. He spends countless hours gazing at the screen, watching the cursor blink, hoping that his carefully crafted words will 
touch the hearts of many. While his possessive nature may make forming deep connections challenging, Harold's mission of artistic recognition through the internet drives him onward, hoping that one day, his brilliance might shine through.
""",
    "name": "Harold Jenkins",
    "age": 55,
    "gender": "male",
}

personas = {"harold_jenkins": harold_jenkins}


def get_persona(id):
    persona_dict = personas[id]
    name = persona_dict["name"]
    description = persona_dict["description"]
    age = persona_dict["age"]
    gender = persona_dict["gender"]
    return name, description, age, gender
