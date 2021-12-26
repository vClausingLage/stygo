import re


with open("tokenizer/input-roman.txt", "r") as f:
  text = f.read()

text = text.replace("[", "")
text = text.replace("]", "")
text = re.sub("[0-9]", "", text)

text = text.split()

data = {"author": "longos", "text": text}


with open("tokenizer/input-roman.json", "w") as f:
  f.write(str(data))