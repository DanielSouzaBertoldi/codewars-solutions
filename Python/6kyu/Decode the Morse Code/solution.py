def decodeMorse(morse_code):
    text = ''
    for words in morse_code.strip().split("  "):
        for word in words.split(' '):
            if word:
                text += MORSE_CODE[word]
            else:
                text += ' '
    return text