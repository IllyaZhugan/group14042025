import string


def make_hashtag(text):

    text = text.translate(str.maketrans("", "", string.punctuation))
    hashtag = "#" + "".join(word.capitalize() for word in text.split())
    return hashtag[:140]


examples = [
    "Python Community",
    "i like python community!",
    "Should, I. subscribe? Yes!",
]

for ex in examples:
    result = make_hashtag(ex)
    print(f"'{ex}' -> {result}")
