import json
from os import altsep
import re
from tokenizer import morphology_generator
from tokenizer import query_tokens_generator
from tokenizer import text_preparer
from tokenizer import noise_terms
from tokenizer import lemma_generator

# To Do
# ENDUNGEN IN JSON !!! ergänzen

# generate TOKENS (lemma) for QUERY
query_tokens = morphology_generator.generateDecl(query_tokens_generator.stems_decl_full)
print("1. query tokens genreated")
# PREPARE text (remove DIACRITICS)
text = text_preparer.text_preparer("tokenizer/input.txt")
print("2. text prepared")
with open("normalizedText.txt", "w") as f:
  f.write(text)
# PREAPARE text (remove NOISE)
text = noise_terms.removeNoise(text, noise_terms.noise_terms)
print("... and noise removed from text")

# prepare QUERY LISTS
angry_list = query_tokens["angry"]["aDecl"] + query_tokens["angry"]["oDecl"] + query_tokens["angry"]["kDecl"]
nasty_list = query_tokens["nasty"]["aDecl"] + query_tokens["nasty"]["oDecl"] + query_tokens["nasty"]["kDecl"]
affectionate_list = query_tokens["affectionate"]["aDecl"] + query_tokens["affectionate"]["oDecl"] + query_tokens["affectionate"]["kDecl"]
nice_list = query_tokens["nice"]["aDecl"] + query_tokens["nice"]["oDecl"] + query_tokens["nice"]["kDecl"]

# QUERY text with tokens
def findToken(text, query_list):
  result = []
  for query in query_list:
    query = query.split()
    count = 0
    for x in query:
      count += len(re.findall(rf'\b{x}\b', text))
    result.append({"query": query[0], "count": count})
  return result
print("3. begin query")
query_tokens["angry"]["result"] = findToken(text, angry_list)
query_tokens["nasty"]["result"] = findToken(text, nasty_list)
query_tokens["affectionate"]["result"] = findToken(text, affectionate_list)
query_tokens["nice"]["result"] = findToken(text, nice_list)

print("4. writing file")
with open("tokenizer/queryTokens.json", "w", encoding='utf8') as f:       # write RESULTS to FILE (necessary?)
  query_tokens = json.dumps(query_tokens, ensure_ascii=False, indent=2)
  f.write(str(query_tokens))

lemmatized_text = lemma_generator.replaceLemmata(text, lemma_generator.lemmata_list)
print("5. testing word frequencies")
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
word_count = word_count(lemmatized_text)
print(word_count[-40:])