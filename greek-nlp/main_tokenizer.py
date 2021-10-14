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

# PREPARE text (remove DIACRITICS)
text = text_preparer.text_preparer("tokenizer/input.txt")

# PREAPARE text (remove NOISE)
text = noise_terms.removeNoise(text, noise_terms.noise_terms)

# PREPARE QUERY LIST
def tokensToList(query_tokens):
  angry_tokens_tmp = []
  nasty_tokens_tmp = []
  affectionate_tokens_tmp = []
  nice_tokens_tmp = []
  # angry_tokens = ""
  # nasty_tokens = ""
  # affectionate_tokens = ""
  # nice_tokens = ""
  [angry_tokens_tmp.append(x) for x in query_tokens["angry"]["aDecl"]]
  [angry_tokens_tmp.append(x) for x in query_tokens["angry"]["oDecl"]]
  [angry_tokens_tmp.append(x) for x in query_tokens["angry"]["kDecl"]]
  # for x in angry_tokens_tmp:
  #   angry_tokens += x
  [nasty_tokens_tmp.append(x) for x in query_tokens["nasty"]["aDecl"]]
  [nasty_tokens_tmp.append(x) for x in query_tokens["nasty"]["oDecl"]]
  [nasty_tokens_tmp.append(x) for x in query_tokens["nasty"]["kDecl"]]
  # for x in nasty_tokens_tmp:
  #   nasty_tokens += x
  [affectionate_tokens_tmp.append(x) for x in query_tokens["affectionate"]["aDecl"]]
  [affectionate_tokens_tmp.append(x) for x in query_tokens["affectionate"]["oDecl"]]
  [affectionate_tokens_tmp.append(x) for x in query_tokens["affectionate"]["kDecl"]]
  # for x in affectionate_tokens_tmp:
  #   affectionate_tokens += x
  [nice_tokens_tmp.append(x) for x in query_tokens["nice"]["aDecl"]]
  [nice_tokens_tmp.append(x) for x in query_tokens["nice"]["oDecl"]]
  [nice_tokens_tmp.append(x) for x in query_tokens["nice"]["kDecl"]]
  # for x in nice_tokens_tmp:
  #   nice_tokens += x
  return [angry_tokens_tmp, nasty_tokens_tmp, affectionate_tokens_tmp, nice_tokens_tmp]
query_list = tokensToList(query_tokens)

#### GET QUERY_LIST
##### TEST IT WITH findToken

# QUERY text with tokens
def findToken(text, query_list):
  # MAKE IT WORK !!!
  # result = []
  # count = 0
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
result_affectionate = findToken(text, query_list[2])
result_nice = findToken(text, query_list[3])
print(result_angry)
print(result_nasty)
print(result_affectionate)
print(result_nice)

# with open("tokenizer/queryTokens.json", "w", encoding='utf8') as f:       # write RESULTS to FILE (necessary?)
#   query_tokens = json.dumps(query_tokens, ensure_ascii=False, indent=2)
#   f.write(str(query_tokens))