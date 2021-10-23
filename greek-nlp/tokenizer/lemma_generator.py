from tokenizer import dediacritcializer as de

endingsK = ["ι", "ος", "α", "ες", "ων", "σι", "σιν", "ας"]
endingsOm = ["ου", "ω", "ον", "οι", "ων", "οις", "ους"]
endingsOn = ["ου", "ω", "ον", "α", "ων", "οις"]
endingsAa = ["αν", "αι", "ων", "αις", "ας"]
endingsAe = ["ης", "ην", "αι", "ων", "αις", "ας"]

def fillLemmata(lemmata): # lemmata : list
  lemmata_list = []
  for lemma in lemmata:
    nom = lemma[0]
    gen = lemma[1]
    nom = de.dediacriticalizer(nom)
    gen = de.dediacriticalizer(gen)
    stem = gen[:-2]
    if nom[-2:] == "ος":
      tokens = [lemma[0]]
      tokens.append(nom)
      for ending in endingsOm:
        tokens.append(stem + ending)
      lemmata_list.append(tokens)
    elif nom[-2:] == "ον":
      tokens = [lemma[0]]
      tokens.append(nom)
      for ending in endingsOn:
        tokens.append(stem + ending)
      lemmata_list.append(tokens)
    elif gen[-2:] == "ος":
      tokens = [lemma[0]]
      tokens.append(nom)
      for ending in endingsK:
        tokens.append(stem + ending)
      lemmata_list.append(tokens)
    elif nom[-1] == "α":
      tokens = [lemma[0]]
      tokens.append(nom)
      for ending in endingsAa:
        tokens.append(stem + ending)
      lemmata_list.append(tokens)
    elif nom[-1] == "η":
      tokens = [lemma[0]]
      tokens.append(nom)
      for ending in endingsAe:
        tokens.append(stem + ending)
      lemmata_list.append(tokens)
    else:
      print("lemma not found")
  return lemmata_list