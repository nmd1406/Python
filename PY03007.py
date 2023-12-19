from sys import stdin


for line in stdin:
    sentence = ""
    for token in line.split():
        if token[-1] == "." or token[-1] == "?" or token[-1] == "!":
            sentence += token[:-1]
            print(sentence.strip().capitalize())
            sentence = ""
        else:
            sentence += token + " "