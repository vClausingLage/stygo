from tokenizer import dediacritcializer

def text_preparer(text):
    with open(text, "r") as file:
        text = file.read()
        text = dediacritcializer.dediacriticalizer(text)
    return text