import json
from os import O_DIRECT
from tokenizer import dediacritcializer

with open('tokenizer/endingsGreek.json', 'r', encoding='utf8') as file:
    endings = file.read()
    endings = json.loads(endings)

endingsO = endings["oDecl"]
endingsA = endings["aDecl"]
endingsK = endings["kDecl"]

def generateDecl(stems_decl):
  for el in stems_decl:
    # O DECL
    if len(stems_decl[el]["oDecl"]) > 0:
      oDecl = stems_decl[el]["oDecl"][0]
      for token in oDecl:
        token_list = []
        size = len(token)
        token = token[:size-2]
        for ending in endingsO:
          input_token = token + ending
          # REMOVE DIACRITICS
          input_token = dediacritcializer.dediacriticalizer(input_token)
          token_list.append(input_token)
        stems_decl[el]["oDecl"].append(" ".join(token_list))
      stems_decl[el]["oDecl"].pop(0)
    # A DECL
    if len(stems_decl[el]["aDecl"]) > 0:
      aDecl = stems_decl[el]["aDecl"][0]
      for token in aDecl:
        token_list = []
        size = len(token)
        token = token[:size-1]
        for ending in endingsA:
          input_token = token + ending
          # REMOVE DIACRITICS
          input_token = dediacritcializer.dediacriticalizer(input_token)
          token_list.append(input_token)
        stems_decl[el]["aDecl"].append(" ".join(token_list))
      stems_decl[el]["aDecl"].pop(0)
    # K DECL
    if len(stems_decl[el]["kDecl"]) > 0:
      kDecl = stems_decl[el]["kDecl"][0]
      for token in kDecl:
        # TO DO IF ELSES FOR ENDINGS!!!
        # TO DO search for "τσ" -> "σ"
        if token[-1] == "α":
          token_list = []
          for ending in endingsK:
            input_token = token + "τ" + ending
            # REMOVE DIACRITICS
            input_token = dediacritcializer.dediacriticalizer(input_token)
            token_list.append(input_token)
          stems_decl[el]["kDecl"].append(" ".join(token_list))
      stems_decl[el]["kDecl"].pop(0)
  return stems_decl