with open('story.txt', 'r') as f:
    story = f.read()

words = set()

target_start = '<'
target_end = '>'

word_started = -1
input_words = {}

for i, char in enumerate(story):
    if char == target_start:
        word_started = i

    if char == target_end and word_started != -1:
        word = story[word_started: i+1]
        words.add(word)
        word_started = -1

for word in words:
    user_word = input(f"Please provide a {word}: ")
    input_words[word] = user_word

for [key, value] in input_words.items():
    story = story.replace(key, value)
