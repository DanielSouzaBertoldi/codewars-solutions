def spin_words(sentence):
    words = []
    for x in sentence.split():
        if len(x) > 4:
            x = x[::-1]
        words.append(x)
    return " ".join(words);