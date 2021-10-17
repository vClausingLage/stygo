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
print("query tokens genreated")
# PREPARE text (remove DIACRITICS)
text = text_preparer.text_preparer("tokenizer/input.txt")
print("text prepared")
# PREAPARE text (remove NOISE)
# text = noise_terms.removeNoise(text, noise_terms.noise_terms)
# print("noise removed from text")

# prepare QUERY LIST
query_list = []
angry_list = query_tokens["angry"]["aDecl"] + query_tokens["angry"]["oDecl"] + query_tokens["angry"]["kDecl"]
nasty_list = query_tokens["nasty"]["aDecl"] + query_tokens["nasty"]["oDecl"] + query_tokens["nasty"]["kDecl"]
affectionate_list = query_tokens["affectionate"]["aDecl"] + query_tokens["affectionate"]["oDecl"] + query_tokens["affectionate"]["kDecl"]
nice_list = query_tokens["nice"]["aDecl"] + query_tokens["nice"]["oDecl"] + query_tokens["nice"]["kDecl"]
query_list.append(angry_list)
query_list.append(nasty_list)
query_list.append(affectionate_list)
query_list.append(nice_list)

# QUERY text with tokens
def findToken(text, query_list):
  print("begin query")
  result = []
  count = 0
  for query in query_list:
    query = query.split()
    for x in query:
      count += len(re.findall(rf'\b{x}\b', text))
      result.append({"query": x[0], "count": count})

  # # for query in query_list:
  # #   if len(query) > 0:
  # #     for el in query:
  # #       count = 0
  # for x in query_list:
  #   count += len(re.findall(rf'\b{x}\b', text))
  #   result.append({"query": x[0], "count": count})
  return result
result_angry = findToken(text, query_list[0])
result_nasty = findToken(text, query_list[1])
# result_affectionate = findToken(text, query_list[2])
# result_nice = findToken(text, query_list[3])
print(result_angry)
print(result_nasty)
# print(result_affectionate)
# print(result_nice)

# with open("tokenizer/queryTokens.json", "w", encoding='utf8') as f:       # write RESULTS to FILE (necessary?)
#   query_tokens = json.dumps(query_tokens, ensure_ascii=False, indent=2)
#   f.write(str(query_tokens))