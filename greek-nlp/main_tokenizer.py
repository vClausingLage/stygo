import json
from tokenizer import morphology_generator
from tokenizer import tokens_to_lemma
from tokenizer import text_preparer
from tokenizer import noise_terms

# generate TOKENS (lemma) for QUERY
query_tokens = morphology_generator.generateDecl(tokens_to_lemma.stems_decl)

# PREPARE text (remove DIACRITICS)
text = text_preparer.text_preparer("tokenizer/input.txt")

# PREAPARE text (remove NOISE)
text = noise_terms.removeNoise(text, noise_terms.noise_terms)


print(text)

# with open("tokenizer/queryTokens.json", "w", encoding='utf8') as f:       # write RESULTS to FILE (necessary?)
#   query_tokens = json.dumps(query_tokens, ensure_ascii=False, indent=2)
#   f.write(str(query_tokens))