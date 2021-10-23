import json
import re
from tokenizer import morphology_generator
from tokenizer import query_tokens_generator
from tokenizer import text_preparer
from tokenizer import noise_terms
from tokenizer import lemma_generator as lem

# PREPARE text (remove DIACRITICS)
text = text_preparer.text_preparer("tokenizer/input.txt")
print("1. text loaded and prepared")
with open("normalizedText.txt", "w") as f:
  f.write(text)
# PREAPARE text (remove NOISE)
text = noise_terms.removeNoise(text, noise_terms.noise_terms)
print("... and noise removed from text")

angry_subst = [("φόβος", "φόβου"), ("πόλεμος", "πολέμου"), ("βλάβη", "βλάβης"), ("ὀργή", "ὀργῆς"), ("αἰσχύνη", "αἰσχύνης"), ("βία", "βίας")] ; angry_adj = [("στυγερός", "στυγεροῦ"), ("ἐχθρός", "ἐχθροῦ")]
nasty_subst = [("ψόγος", "ψόγου"), ("δεῖμα", "δείματος")]; nasty_adj = [("κακός", "κακοῦ")]
affectionate_subst = [("φίλος", "φίλου"), ("γάμος", "γάμου"), ("σωτήρ", "σωτήρος")]; affectionate_adj = []
nice_subst = [("χαρις", "χάριτος")]; nice_adj = [("καλός", "καλοῦ")]

angry = lem.fillLemmata(angry_subst) + lem.fillLemmata(angry_adj)
nasty = lem.fillLemmata(nasty_subst) + lem.fillLemmata(nasty_adj)
affectionate = lem.fillLemmata(affectionate_subst) + lem.fillLemmata(affectionate_adj)
nice = lem.fillLemmata(nice_subst) + lem.fillLemmata(nice_adj)

lemmata = {"angry": angry, "nasty": nasty, "affectionate": affectionate, "nice": nice}

def lemmatizeText(text, lemmata):
  all_lemmata = lemmata["angry"] + lemmata["nasty"] + lemmata["affectionate"] + lemmata["nice"]
  for element in all_lemmata:
    for lemma in element:
      # print(lemma)
      text = re.sub(rf"\b{lemma}\b", element[1], text) # text.replace(lemma, element[1])
  return text
print("2. lemmatizing text")
lemmatized_text = lemmatizeText(text, lemmata)
print("writing file...")
with open("lemmatizedText.txt", "w") as f:
  f.write(lemmatized_text)

def findToken(text, query_list):
  result = []
  count = 0
  for query in query_list:
    for el in query:
      count += len(re.findall(rf"\b{el}\b", text))
    result.append(query[0])
  return {"tokens": result, "result": count}
print("3. finding tokens")
results = {"angry": findToken(text, angry), "nasty": findToken(text, nasty), "affectionate": findToken(text, affectionate), "nice": findToken(text, nice)}

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
  f.write(str(word_count(lemmatized_text)))