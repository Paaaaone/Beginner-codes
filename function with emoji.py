def emoji(sentence_emoji):
    word = sentence_emoji.split(" ")
    output = ""
    character = {
        ":)": "smiley",
        ":(": "sadly"
    }
    for ch in word:
        output += character.get(ch, ch) + " "
    return output


sentence = input("> ")
out = emoji(sentence)
print(out)
