# To Do
# remove diacritics double ?

import json
from tokenizer import dediacritcializer

with open('tokenizer/endingsGreek.json', 'r', encoding='utf8') as file:
    endings = file.read()
    endings = json.loads(endings)

endingsO = endings["oDecl"]
endingsA = endings["aDecl"]

def generateDecl(stems_decl):
  # list for n elements of stems_decl
  stems_decl_list = [[]] * len(stems_decl)
  # oDecl
  oDecl = []
  if (len(stems_decl["oDecl"])) > 0:
    oDecl = stems_decl["oDecl"].split()
  tokens = []
  for token in oDecl:
    token_list = []
    size = len(token)
    token = token[:size-2]
    for ending in endingsO:
      input_token = token + ending
      # REMOVE DIACRITICS
      input_token = dediacritcializer.dediacriticalizer(input_token)
      token_list.append(input_token)
    tokens.append(token_list)
  stems_decl_list[1] = tokens
  # aDecl
  oDecl = []
  if (len(stems_decl["aDecl"])) > 0:
    oDecl = stems_decl["aDecl"].split()
  for token in oDecl:
    tokens = []
    size = len(token)
    token = token[:size-1]
    # REMOVE DIACRITICS
    token = dediacritcializer.dediacriticalizer(token)
    for ending in endingsA:
      input_token = token + ending
      # # REMOVE DIACRITICS
      input_token = dediacritcializer.dediacriticalizer(input_token)
      tokens.append(input_token)
    stems_decl_list[0] = tokens
  # returns LIST of new TOKENS
  return stems_decl_list