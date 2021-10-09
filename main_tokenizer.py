import json
from tokenizer import morphology_generator
from tokenizer import tokens_stem
from tokenizer import text_preparer



query_tokens = morphology_generator.generateDecl(tokens_stem.stems_decl)

# text = text_preparer.text_preparer("tokenizer/input.txt")
# print(text)

with open("tokenizer/queryTokens.json", "w", encoding='utf8') as f:
  query_tokens = json.dumps(query_tokens, ensure_ascii=False, indent=2)
  f.write(str(query_tokens))