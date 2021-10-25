import re
import json
from tokenizer import dediacritcializer

def joinWords(query_string):
  for index,string in enumerate(query_string):
    string.strip()
    if string[-1] == "-":
      string = list(string)
      string.remove("-")
      string = "".join(string)
      query_string[index] = string
      query_string[index] = query_string[index] + query_string[index + 1]
      query_string.pop(index + 1)
  query_string = " ".join(query_string)
  return query_string

def text_preparer(text):
      text = joinWords(text)
      # remove white space
      text = re.sub(" {2,}", " ", text)
      # remove NUMBERS
      text = re.sub("\d", "", text)
      # remove PUNCTUATION
      text = re.sub("[.,:;-]", "", text)
      # remove DIACRITICS
      text = dediacritcializer.dediacriticalizer(text)
      return text