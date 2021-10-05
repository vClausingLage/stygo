import re
import json
from angry_strings import *
from noise_terms import noise_terms

# get text from JSON
with open('tragedistsTexts.json', 'r', encoding='utf8') as file:
    data = file.read()
    data = json.loads(data)
    if data[0]["author"] == "aeschylus":
      aeschylus_text = data[0]["text"]
      print("Aeschylus safe")
    if data[1]["author"] == "sophocles":
      sophocles_text = data[1]["text"]
      print("Sophocles safe")
    if data[2]["author"] == "euripides":
      euripides_text = data[2]["text"]
      print("Euripides safe")

# compose strings
aeschylus_text = " ".join(aeschylus_text)
sophocles_text = " ".join(sophocles_text)
euripides_text = " ".join(euripides_text)

# remove non semantic tokens
def removeNoise(query_string, noise_terms):
 noise_terms = noise_terms.strip()
 noise_terms = noise_terms.split()
 for term in noise_terms:
   query_string = re.sub(rf'\b{term}\b', '', query_string)
 return query_string

aeschylus_text = removeNoise(aeschylus_text, noise_terms)
sophocles_text = removeNoise(sophocles_text, noise_terms)
euripides_text = removeNoise(euripides_text, noise_terms)

# join disjunct tokens
def joinWords(query_string):
 query_string = re.sub('-\s', '', query_string)
 return query_string

aeschylus_text = joinWords(aeschylus_text)
sophocles_text = joinWords(sophocles_text)
euripides_text = joinWords(euripides_text)

aeschylus_text_total = len(aeschylus_text)
sophocles_text_total = len(sophocles_text)
euripides_text_total = len(euripides_text)

# To Do 
# REMOVE EXCEPTIONS
# def removeExceptions(query_string):
#   print('hello')
# angry_str = removeExceptions(angry_str)
# nasty_str = removeExceptions(nasty_str)
# affectionate_str = removeExceptions(affectionate_str)
# nice_str = removeExceptions(nice_str)
# find words of ANGER and LOVE
def findAnger(text, query_str):
  result = []
  query_str = query_str.split()
  for query in query_str:
    result = result + re.findall(rf'\b{query}\w+', text)
  return result
# Aeschylus
aeschylus_anger = len(findAnger(aeschylus_text, angry_str))
aeschylus_nasty = len(findAnger(aeschylus_text, nasty_str))
aeschylus_affectionate = len(findAnger(aeschylus_text, affectionate_str))
aeschylus_nice = len(findAnger(aeschylus_text, nice_str))
# Sophocles
sophocles_anger = len(findAnger(sophocles_text, angry_str))
sophocles_nasty = len(findAnger(sophocles_text, nasty_str))
sophocles_affectionate = len(findAnger(sophocles_text, affectionate_str))
sophocles_nice = len(findAnger(sophocles_text, nice_str))
# Euripides
euripides_anger = len(findAnger(euripides_text, angry_str))
euripides_nasty = len(findAnger(euripides_text, nasty_str))
euripides_affectionate = len(findAnger(euripides_text, affectionate_str))
euripides_nice = len(findAnger(euripides_text, nice_str))

# get total counts
# for TESTING TOKENS
def word_count(query_string):
   counts = dict()
   words = query_string.split()
   for word in words:
       if word in counts:
           counts[word] += 1
       else:
           counts[word] = 1
   counts = sorted(counts.items(), key=lambda item: item[1])
   return counts
# PRINT TOTAL TOKENS // FOR WORDCLOUD
aeschylus_tokens = word_count(aeschylus_text)
sophocles_tokens = word_count(sophocles_text)
euripides_tokens = word_count(euripides_text)
# PRINT SPECIAL TOKENS
# print('anger', findAnger(aeschylus_text, angry_str))
# print('nasty',findAnger(aeschylus_text, nasty_str))
# print('affectionate',findAnger(aeschylus_text, affectionate_str))
# print('nice',findAnger(aeschylus_text, nice_str))

# WRITE TO FILE
with open('tragedistsData.json', 'w', encoding='utf8') as file:
 data = [
   {"author": "aeschylus", "total": aeschylus_text_total, "angry": aeschylus_anger / aeschylus_text_total, "nasty": aeschylus_nasty / aeschylus_text_total , "affectionate": aeschylus_affectionate / aeschylus_text_total , "nice": aeschylus_nice / aeschylus_text_total , "tokens": aeschylus_tokens},
   {"author": "sophocles", "total": sophocles_text_total, "angry": sophocles_anger / sophocles_text_total, "nasty": sophocles_nasty / sophocles_text_total , "affectionate": sophocles_affectionate / sophocles_text_total , "nice": sophocles_nice / sophocles_text_total , "tokens": sophocles_tokens},
   {"author": "euripides", "total": euripides_text_total, "angry": euripides_anger / euripides_text_total, "nasty": euripides_nasty / euripides_text_total , "affectionate": euripides_affectionate / euripides_text_total , "nice": euripides_nice / euripides_text_total , "tokens": euripides_tokens}
 ]
 output = json.dumps(data, ensure_ascii=False)
 file.write(output)