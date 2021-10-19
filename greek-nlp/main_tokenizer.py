import json
from os import altsep
import re
from tokenizer import morphology_generator
from tokenizer import query_tokens_generator
from tokenizer import text_preparer
from tokenizer import noise_terms

# To Do
# getrennte Wörter verbinden!
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
# text = noise_terms.removeNoise(text, noise_terms.noise_terms)
# print("noise removed from text")

# prepare QUERY LISTS
angry_list = query_tokens["angry"]["aDecl"] + query_tokens["angry"]["oDecl"] + query_tokens["angry"]["kDecl"]
nasty_list = query_tokens["nasty"]["aDecl"] + query_tokens["nasty"]["oDecl"] + query_tokens["nasty"]["kDecl"]
affectionate_list = query_tokens["affectionate"]["aDecl"] + query_tokens["affectionate"]["oDecl"] + query_tokens["affectionate"]["kDecl"]
nice_list = query_tokens["nice"]["aDecl"] + query_tokens["nice"]["oDecl"] + query_tokens["nice"]["kDecl"]

# QUERY text with tokens
def findToken(text, query_list):
  result = []
  count = 0
  for query in query_list:
    query = query.split()
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