from tokenizer import greek_morphology_generator
from tokenizer import tokens_stem
from tokenizer import text_preparer

test = greek_morphology_generator.generateDecl(tokens_stem.stems_decl)

# text = text_preparer.text_preparer("tokenizer/input.txt")
# print(text)

print(test)
