import random

def getrandom():
    animals = ["lion", "fox", "cat", "dog", "dolphin", "cheetah", "bird", "horse", "rabbit", "elephant"]
    actions = ["jumped", "sat", "ran", "climbed", "crawled", "flew", "swam", "walked"]
    adverbs = ["very slowly", "quickly", "gracefully", "clumsily", "silently", "noisily", "cheerfully", "angrily", "nervously", "happily"]

    animal = random.choice(animals)
    action = random.choice(actions)
    adverb = random.choice(adverbs)

    sentence = f"The {animal} {action} {adverb}"

    print(sentence)

getrandom()
