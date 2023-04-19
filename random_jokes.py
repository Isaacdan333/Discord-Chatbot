import random

def random_insult():
    random_list = [
        "Need to touch grass",
        "Will never get a real girlfriend",
        "Will never get a real boyfriend",
        "We can smell the degenerate on you",
        "You sick freak",
        "You forgot to take a bath",
        "Filthy casual",
        "I can smell the mustiness off of you",
        "If I speak what is on my mind, I will get arrested.",
        "Average league of legends player.",
        "KYS... which stands for Keep Yourself Safe :)",
        "...",
        "I have no words",
        "Whatever happened to shame?",
        "Thanos was right.",
        "Why are you like this?",
    ]
    list_count = len(random_list)
    random_item = random.randrange(list_count)
    return random_list[random_item]

#print(random_string())