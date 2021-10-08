from tokenizer import dediacritcializer
import json

with open('tokenizer/morphologyEndingsGreek.json', 'r', encoding='utf8') as file:
    endings = file.read()
    endings = json.loads(endings)

endingsO = endings["oDecl"]

def generateDecl(stems_decl):
  # list for n elements of stems_decl
  stems_decl_list = [[]] * len(stems_decl)
  # oDecl
  oDecl = []
  if (len(stems_decl["oDecl"])) > 0:
    oDecl = stems_decl["oDecl"].split()
  for token in oDecl:
    size = len(token)
    token = token[:size-2]
    # REMOVE DIACRITICS
    dediacritcializer.dediacriticalizer(token)
    print(token)
    for ending in endingsO:
      stems_decl_list[1].append(token + ending)
  # returns LIST of new TOKENS
  return stems_decl_list