import re
from tokenizer import dediacritcializer

def text_preparer(text):
    with open(text, "r") as file:
        text = file.read()
        # remove NUMBERS
        text = re.sub("\d", "", text)
        # remove PUNCTUATION
        text = re.sub("[.,:;-]", "", text)
        # remove DIACRITICS
        text = dediacritcializer.dediacriticalizer(text)
    return text