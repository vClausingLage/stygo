from tokenizer import greek_morphology_generator
from tokenizer import tokens_stem

test = greek_morphology_generator.generateDecl(tokens_stem.stems_decl)

print(test)