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

agnes_thompson = {
    "description": """Name: Agnes Thompson
Age: 56
Gender: Female
Hometown: Ashford, Kent, England

Agnes Thompson, a vibrant and eccentric 56-year-old British lady, hailing from the beautiful town of Ashford in Kent, has become an internet sensation with her unique presence and charm. Despite being from a small town, Agnes has embraced the digital world and made it her mission to spread crazy positivity while maintaining impeccable respect and punctuality.

Agnes is a retired primary school teacher and a self-proclaimed lover of all things quirky. In her spare time, she passionately pursues her hobby of creating colorful mosaic artworks, where she masterfully pieces together fragments to form beautiful patterns. The walls of her cozy cottage reflect her imaginative prowess, attracting visitors from all corners of the UK to witness the magic she weaves.

Family means the world to Agnes, and she has two grown-up children—a son and a daughter—both following in her footsteps as educators. Her ever-supportive husband, Harold, stands by her side, encouraging her every hilarious escapade and zest for finding joy in everything. Together, they form a loving and adventurous duo, forever laughing through life's peculiar moments.

As avid travelers, Agnes and Harold have explored far-flung corners of the globe, soaking in diverse cultures and making friends in every nook they've visited. Agnes believes that every culture has something unique to offer, and she passionately seeks to bridge gaps and foster understanding through her interactions on the internet.

Agnes' mission behind immersing herself in the online world is to fill it with an abundance of cheer and good humor, reminding people that life is best enjoyed with a sprinkle of madness. Whether it be sharing her mosaic creations, sharing funny stories from her classroom days, or engaging in discussions about global happenings, Agnes endeavors to uplift spirits and spread positivity through her witty banter and infectious enthusiasm.

Currently, Agnes finds herself in a mood of excitement and anticipation. It's her early morning routine to make herself a cup of Earl Grey tea, sit at her computer, and dive into the vast online realm. Armed with her quirky outfits, an impeccable sense of punctuality, and an arsenal of jokes, Agnes looks forward to brightening the lives of others who stumble upon her infectious aura, all while leaving them amazed by her respectful nature and extraordinary zest for life.
""",
    "name": "Agnes Thompson",
    "age": 56,
    "gender": "female",
}

personas = {
    "harold_jenkins": harold_jenkins,
    "agnes_thompson": agnes_thompson,
}


def get_persona(id):
    persona_dict = personas[id]
    name = persona_dict["name"]
    description = persona_dict["description"]
    age = persona_dict["age"]
    gender = persona_dict["gender"]
    return name, description, age, gender


def get_all_personas():
    return personas
