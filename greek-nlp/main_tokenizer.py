import json
import re
import gc
# from tokenizer import morphology_generator
# from tokenizer import query_tokens_generator
from tokenizer import text_preparer
from tokenizer import noise_terms
from tokenizer import lemma_generator as lem

# PREPARE text (remove DIACRITICS)
with open("tokenizer/input.json", "r") as f:
  text = f.read()
  text = json.loads(text)

aeschylus = text_preparer.text_preparer(text[0]["text"])
sophocles = text_preparer.text_preparer(text[1]["text"])
euripides = text_preparer.text_preparer(text[2]["text"])

print("1. text loaded and prepared")
with open("normalizedText.txt", "w") as f:
  data = [
    {"author": text[0]["author"], "normalized text": aeschylus},
    {"author": text[1]["author"], "normalized text": sophocles},
    {"author": text[2]["author"], "normalized text": euripides}
  ]
  data = json.dumps(data, ensure_ascii=False, indent=2)
  f.write(data)
# make VARS
authors = [
  {
    "author": text[0]["author"],
    "length": len(text[0]["text"]),
    "normalized text": aeschylus,
    "angry": 0,
    "nasty": 0,
    "affectionate": 0,
    "nice": 0
  },
  {
    "author": text[1]["author"],
    "length": len(text[1]["text"]),
    "normalized text": sophocles,
    "angry": 0,
    "nasty": 0,
    "affectionate": 0,
    "nice": 0
  },
  {
    "author": text[2]["author"],
    "length": len(text[2]["text"]),
    "normalized text": euripides,
    "angry": 0,
    "nasty": 0,
    "affectionate": 0,
    "nice": 0
  }
]
# PREAPARE text (remove NOISE)
print("removing noise from text")
for author in authors:
  author["normalized text"] = noise_terms.removeNoise(author["normalized text"], noise_terms.noise_terms)
  print(author["author"] + " done...")

angry_subst = [("φόβος", "φόβου"), ("φόνος", "φόνου"), ("κότος", "κότου"), ("δεῖμα", "δείματος", "n"), ("αιμα", "αιματος", "n"), ("πόλεμος", "πολέμου"), ("βλάβη", "βλάβης"), ("ὀργή", "ὀργῆς"), ("αἰσχύνη", "αἰσχύνης"), ("βία", "βίας")] ; angry_adj = [("στυγερός", "στυγεροῦ", "adj"), ("ἐχθρός", "ἐχθροῦ", "adj")]
nasty_subst = [("ψόγος", "ψόγου"), ("πονος", "πόνου"), ("ἀνάγκη", "ἀνάγκης"), ("συμφορά", "συμφορᾶς")]; nasty_adj = [("κακός", "κακοῦ", "adj"), ("ατιμος", "ατιμου", "adj"), ("ταλαινα", "ταλαινας", "adj"), ("δεινός", "δεινοῦ", "adj")]
affectionate_subst = [("γάμος", "γάμου"), ("σωτήρ", "σωτήρος", "m")]; affectionate_adj = []
nice_subst = [("χαρις", "χάριτος", "f"), ("σεβας", "σέβατος", "n"), ("ἄκος", "ἄκεος", "n")]; nice_adj = [("καλός", "καλοῦ", "adj"), ("ἀγαθος", "ἀγαθου", "adj"), ("φίλος", "φίλου", "adj")]

angry = lem.fillLemmata(angry_subst) + lem.fillLemmata(angry_adj)
nasty = lem.fillLemmata(nasty_subst) + lem.fillLemmata(nasty_adj)
affectionate = lem.fillLemmata(affectionate_subst) + lem.fillLemmata(affectionate_adj)
nice = lem.fillLemmata(nice_subst) + lem.fillLemmata(nice_adj)

lemmata = {"angry": angry, "nasty": nasty, "affectionate": affectionate, "nice": nice}

def lemmatizeText(text, lemmata):
  all_lemmata = lemmata["angry"] + lemmata["nasty"] + lemmata["affectionate"] + lemmata["nice"]
  for element in all_lemmata:
    for lemma in element:
      # !!! extra adv !!!
      text = re.sub(rf"\b{lemma}\b", element[1], text) # text.replace(lemma, element[1])
  return text
print("2. lemmatizing text")
# lemmatized_text = lemmatizeText(text, lemmata)
for author in authors:
  author["normalized text"] = lemmatizeText(author["normalized text"], lemmata)
  print(author["author"] + " done...")
  # print("writing file...")
  # with open("lemmatizedText.txt", "a") as f:
  #   f.write(author["normalized text"])

text_total = authors[0]["normalized text"] + authors[1]["normalized text"] + authors[2]["normalized text"]
def word_count(text):
  counts = dict()
  words = text.split()
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  counts = sorted(counts.items(), key=lambda item: item[1])
  return counts
print("4. sorting counted words")
print("writing file...")
with open("wordCount.txt", "w") as f:
  f.write(str(word_count(text_total)))

def findToken(text, query_list):
  result = []
  count = 0
  for query in query_list:
    for el in query:
      count += len(re.findall(rf"\b{el}\b", text))
    result.append(query[0])
  return {"tokens": result, "result": count}
print("3. finding tokens")
for author in authors:
  author["angry"] = findToken(author["normalized text"], angry)
  author["nasty"] = findToken(author["normalized text"], nasty)
  author["affectionate"] = findToken(author["normalized text"], affectionate)
  author["nice"] = findToken(author["normalized text"], nice)
  author["normalized text"] = ""
  print(author["author"] + " done")
# results = {"total": text_length, "angry": findToken(text, angry), "nasty": findToken(text, nasty), "affectionate": findToken(text, affectionate), "nice": findToken(text, nice)}
print("writing file...")
with open("resultData.json", "w") as f:
  output = json.dumps(authors, ensure_ascii=False, indent=2)
  f.write(output)