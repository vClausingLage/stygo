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
# text length
text_length = len(text.split())

angry_subst = [("φόβος", "φόβου"), ("κότος", "κότου"), ("δεῖμα", "δείματος", "n"), ("πόλεμος", "πολέμου"), ("βλάβη", "βλάβης"), ("ὀργή", "ὀργῆς"), ("αἰσχύνη", "αἰσχύνης"), ("βία", "βίας")] ; angry_adj = [("στυγερός", "στυγεροῦ"), ("ἐχθρός", "ἐχθροῦ")]; angry_add = []
nasty_subst = [("ψόγος", "ψόγου"), ("πονος", "πόνου")]; nasty_adj = [("κακός", "κακοῦ"), ("ατιμος", "ατιμου"), ("ταλαινα", "ταλαινας")]; nasty_add = ["κακά"]
affectionate_subst = [("φίλος", "φίλου"), ("γάμος", "γάμου"), ("σωτήρ", "σωτήρος", "m")]; affectionate_adj = []; affectionate_add = []
nice_subst = [("χαρις", "χάριτος", "f"), ("σεβας", "σέβατος", "n"), ("ἄκος", "ἄκεος", "n")]; nice_adj = [("καλός", "καλοῦ")]; nice_add = []

angry = lem.fillLemmata(angry_subst) + lem.fillLemmata(angry_adj) + angry_add
nasty = lem.fillLemmata(nasty_subst) + lem.fillLemmata(nasty_adj) + nasty_add
affectionate = lem.fillLemmata(affectionate_subst) + lem.fillLemmata(affectionate_adj) + affectionate_add
nice = lem.fillLemmata(nice_subst) + lem.fillLemmata(nice_adj) + nice_add

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
results = {"total": text_length, "angry": findToken(text, angry), "nasty": findToken(text, nasty), "affectionate": findToken(text, affectionate), "nice": findToken(text, nice)}
print("writing file...")
with open("resultData.json", "w") as f:
  output = json.dumps(results, ensure_ascii=False, indent=2)
  f.write(output)

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