import json
import re
from tokenizer import morphology_generator
from tokenizer import query_tokens_generator
from tokenizer import text_preparer
from tokenizer import noise_terms

# To Do
# getrennte Wörter verbinden!

# generate TOKENS (lemma) for QUERY
query_tokens = morphology_generator.generateDecl(query_tokens_generator.stems_decl)

# PREPARE text (remove DIACRITICS)
text = text_preparer.text_preparer("tokenizer/input.txt")

# PREAPARE text (remove NOISE)
text = noise_terms.removeNoise(text, noise_terms.noise_terms)

# QUERY text with tokens
def findToken(text, query_list):
  result = []
  for query in query_list:
    if len(query) > 0:
      for el in query:
        count = 0
        for x in el:
          count += len(re.findall(rf'\b{x}\b', text))
        result.append({"query": el[0], "count": count})
  return result
result = findToken(text, query_tokens)
print(result)

# with open("tokenizer/queryTokens.json", "w", encoding='utf8') as f:       # write RESULTS to FILE (necessary?)
#   query_tokens = json.dumps(query_tokens, ensure_ascii=False, indent=2)
#   f.write(str(query_tokens))