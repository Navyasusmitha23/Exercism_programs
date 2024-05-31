def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabets:
        if char not in sentence:
            return False
    return True
